"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpRequest
from app.models import Lobby,Game,Question,Answer
import random 
from math import factorial
from django.db import connection

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':'2023',
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':'2023',
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':'2023',
        }
    )

def create_lobby(request, n_players):
    n_players=int(n_players)
    u_id=request.user.id
    n_questions=factorial(n_players)//(factorial(n_players-2)*2)
    quests=list(Question.objects.values_list('id',flat='True'))
    quests=random.sample(quests,n_questions)
    g=Game.objects.create(n_questions=n_questions)

    cur=connection.cursor()
    for i in range(1,n_questions+1):                    #kostil
        req=f'Update app_game Set q{i} = {quests[i-1]}  where id={g.id}'        
        cur.execute(req)

    l=Lobby.objects.create(player1=u_id,is_active=True,n_players=n_players,game=g)
    cur.execute(f'SELECT username from auth_user where id={u_id}')
    uname=cur.fetchone()
    #cur.close()
    return render(
        request,
        'app/create_lobby.html',
        {
            'n_players':n_players,
            'lobby_id':l.id,
            'lobby':l,
            'uname':uname[0],
            'title':'About',
            'message':'Your application description page.',
            'year':'2023',
        }
    )
def show_lobby(request,lobby_number):
    lobby=Lobby.objects.get(id=lobby_number)
    players=[]
    players.append(lobby.player1)
    players.append(lobby.player2)
    players.append(lobby.player3)
    players.append(lobby.player4)
    players.append(lobby.player5)
    players.append(lobby.player6)        
    n_conected=0
    while len(players)>lobby.n_players:
        players.pop()
    cur=connection.cursor()
    for i in range(lobby.n_players):
        if players[i] is not None and type(players[i])==type(1):
            cur.execute(f'select username from auth_user where id={players[i]}')
            t=cur.fetchone()
            players[i]=t[0]
            n_conected+=1
    return render(
        request,
        'app/show_lobby.html',
        {
            'n_players':lobby.n_players,
            'lobby_id':lobby.id,
            'lobby':lobby,
            'players':players,
            'conected':n_conected,
            'title':'About',
            'message':'Your application description page.',
            'year':'2023',
        }
    )
def lobby_list(request):
    lobies=Lobby.objects.filter(is_active=1)
    lobby_result=[]
    for l in lobies:
        n_conected=0
        players=[]
        x={}
        players.append(l.player1)
        players.append(l.player2)
        players.append(l.player3)
        players.append(l.player4)
        players.append(l.player5)
        players.append(l.player6)
        for i in range(l.n_players):
            if players[i] is not None:            
                n_conected+=1
        if n_conected<l.n_players:
            x['id']=l.id
            x['n_players']=l.n_players
            x['n_conected']=n_conected
            lobby_result.append(x)
        #print(lobby_result)
    return render(
        request,
        'app/lobby_list.html',
        {
            'lobbys':lobby_result,
            'title':'About',
            'message':'Your application description page.',
            'year':'2023',
        }
    )
def lobby_join(request,lobby_number,n_connected):
    lobby=Lobby.objects.get(id=lobby_number)
    n_connected=int(n_connected)
    players=[]
    players.append(lobby.player1)
    players.append(lobby.player2)
    players.append(lobby.player3)
    players.append(lobby.player4)
    players.append(lobby.player5)
    players.append(lobby.player6)
    if request.user.id in players:
        return show_lobby(request,lobby_number)
    if n_connected==1:
        lobby.player2=request.user.id
        lobby.save()
    elif n_connected==2:
        lobby.player3=request.user.id
        lobby.save()
    elif n_connected==3:
        lobby.player4=request.user.id
        lobby.save()
    elif n_connected==4:
        lobby.player5=request.user.id
        lobby.save()
    elif n_connected==5:
        lobby.player6=request.user.id
        lobby.save()
    return show_lobby(request,lobby_number)

def end_game(request,lobby_id):
    lobby=Lobby.objects.get(id=lobby_id)
    players=[]
    players.append(lobby.player1)
    players.append(lobby.player2)
    players.append(lobby.player3)
    players.append(lobby.player4)
    players.append(lobby.player5)
    players.append(lobby.player6)        
    while len(players)>lobby.n_players:
        players.pop()
    players=dict.fromkeys(players,0)
    answ=Answer.objects.filter(lobby=lobby)
    for a in answ:
        players[a.player1]+=a.score1
        players[a.player2]+=a.score2
    sorted_values = sorted(players.values()) # Sort the values
    sorted_players = {}
    for i in sorted_values:
        for k in players.keys():
            if players[k] == i:
                sorted_players[k] = players[k]
    cur=connection.cursor()
    result=[]
    for k in sorted_players:
        cur.execute(f'select username from auth_user where id={k}')
        t=cur.fetchone()
        x={}
        x['user']=t[0]
        x['score']=sorted_players[k]
        result.append(x)
    return render(
            request,
            'app/endgame.html',
            {
                'title':'Waiting',
                'lobby':lobby_id,
                'result':result,
                'message':f'Game number {lobby_id}',
                'year':'2023',
            }
        )
    

def wait_votes(request,lobby_id):
    lobby=Lobby.objects.get(id=lobby_id)
    if lobby.voted>=lobby.n_players:
        return redirect('end_game',lobby_id=lobby_id)
    else:
        return render(
            request,
            'app/wait_votes.html',
            {
                'title':'Waiting',
                'lobby':lobby_id,
                'message':f'Game number {lobby_id}',
                'year':'2023',
            }
        )

def rate_answers(request,lobby_id):
    if request.method=='GET':
        lobby=Lobby.objects.get(id=lobby_id)
        if Answer.objects.filter(lobby=lobby).exists():
            result=Answer.objects.filter(lobby=lobby)
            r1=result.exclude(player1=request.user.id)
            r1=r1.exclude(player2=request.user.id)
            return render(
                request,
                'app/rate_answers.html',
                {
                    'quest':r1,
                    'lobby':lobby,
                    'title':'Game',
                    'message':f'Game number {lobby_id}',
                    'year':'2023',
                }
            )
    else:
        answ=dict(request.POST)
        lob=Lobby.objects.get(id=lobby_id)
        lob.voted+=1
        lob.save()
        answ.pop('csrfmiddlewaretoken')
        print(answ)
        for id in answ:
            if answ[id][0]=='1':
                t=Answer.objects.get(id=int(id))
                t.score1+=1
                t.save()
            elif answ[id][0]=='2':
                t=Answer.objects.get(id=int(id))
                t.score2+=1
                t.save()
        return redirect('wait_votes',lobby_id=lobby_id)

def wait_answers(request,lobby_id):
    lobby=Lobby.objects.get(id=lobby_id)
    answers_text1=Answer.objects.filter(lobby=lobby).values_list('answ1',flat=True)
    answers_text2=Answer.objects.filter(lobby=lobby).values_list('answ2',flat=True)
    if None not in answers_text1 and None not in answers_text2:
        #print(answers_text1,answers_text2,request.method)
        return redirect('rate_answers',lobby_id=lobby_id)
    else:
        #print(answers_text1,answers_text2,request.method)
        return render(
            request,
            'app/wait_answers.html',
            {
                'title':'Waiting',
                'lobby':lobby_id,
                'message':f'Game number {lobby_id}',
                'year':'2023',
            }
        )

def start_game(request,lobby_id):
    if request.method=='GET':
        return start_game_get(request,lobby_id)
    else:
        answ=dict(request.POST)
        answ.pop('csrfmiddlewaretoken')
        for jk,jv in answ.items():
            if jv[0]=='':
                s='0_empty'
            else:
                s=jv[0]
            i=int(jk)
            answer_item=Answer.objects.get(id=i)
            if answer_item.player1==request.user.id:
                answer_item.answ1=s
                answer_item.save()
            elif answer_item.player2==request.user.id:
                answer_item.answ2=s
                answer_item.save()
        return redirect('wait_answers',lobby_id=lobby_id)

def start_game_get(request,lobby_id):
    lobby=Lobby.objects.get(id=lobby_id)
    #lobby.is_active=False
    #lobby.save()
    if Answer.objects.filter(lobby=lobby).exists():
        result=Answer.objects.filter(lobby=lobby)
        r1=result.filter(player1=request.user.id)
        r2=result.filter(player2=request.user.id)
        r1=r1.union(r2)
        #print(r1,r2,request.user.id,result)
        return render(
            request,
            'app/game_start.html',
            {
                'quest':r1,
                'lobby':lobby,
                'title':'Game',
                'message':f'Game number {lobby_id}',
                'year':'2023',
            }
        )
    g=lobby.game
    players=[]
    players.append(lobby.player1)
    players.append(lobby.player2)
    players.append(lobby.player3)
    players.append(lobby.player4)
    players.append(lobby.player5)
    players.append(lobby.player6)        
    while len(players)>lobby.n_players:
        players.pop()
    questions=[]
    questions.append(g.q1)
    questions.append(g.q2)
    questions.append(g.q3)
    questions.append(g.q4)
    questions.append(g.q5)
    questions.append(g.q6)
    questions.append(g.q7)
    questions.append(g.q8)
    questions.append(g.q9)
    questions.append(g.q10)
    questions.append(g.q11)
    questions.append(g.q12)
    questions.append(g.q13)
    questions.append(g.q14)
    questions.append(g.q15)
    while len(questions)>g.n_questions:
        questions.pop()
    q=0
    for i in range(lobby.n_players-1):
        for j in range(i+1,lobby.n_players):
            Answer.objects.create(player1=players[i],player2=players[j],
                                  lobby=lobby,question=Question.objects.get(id=questions[q]))
            q+=1
    result=Answer.objects.filter(lobby=lobby)
    r1=result.filter(player1=request.user.id)
    r2=result.filter(player2=request.user.id)
    r1=r1.union(r2)
    return render(
        request,
        'app/game_start.html',
        {
            'quest':r1,
            'lobby':lobby,
            'title':'Game',
            'message':f'Game number {lobby_id}',
            'year':'2023',
        }
    )