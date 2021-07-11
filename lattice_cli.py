A0='| {} | {} | {} | {} | {} | {} | {} | {} | {} |\n\n'
z='y'
y=tuple
x=all
w=range
T=input
P=True
O=len
L=False
A=print
import os,random as M,time as I
Z='r'
a='g'
b='b'
c='c'
d='p'
e=z
f='1'
g='2'
h='3'
i='4'
j='5'
k='6'
U=[Z,a,b,c,d,e]
V=[f,g,h,i,j,k]
def l():
	A=[]
	for B in U:
		for C in V:A.append((B,C))
	return A*2
B='0','0'
W=[(0,0),(1,1),(2,2),(0,4),(0,8),(1,7),(2,6),(4,8),(8,0),(7,1),(6,2),(4,0),(8,8),(7,7),(6,6),(8,4)]
m=9
Q=9
def n():
	A={}
	for C in w(Q):
		for D in w(m):A[(C,D)]=B
	return A
def o(tileset):
	B=tileset;E='|{}|'*O(B);C=[]
	for D in B:C.append(f"{D[0]}:{D[1]}")
	A(E.format(*C))
def p(board):
	D=A0*Q;B=[]
	for C in board.values():B.append(f"{C[0]}:{C[1]}")
	A(D.format(*B))
def q(board):
	D=A0*Q;C=[]
	for B in board.keys():
		if B in W:C.append(f"{B[0]}${B[1]}")
		else:C.append(f"{B[0]}:{B[1]}")
	A(D.format(*C))
def r(board,color,pattern,column,row):L=None;G=pattern;F=color;E=row;D=column;C=board;H=B if C.get((D-1,E))is L else C.get((D-1,E));I=B if C.get((D,E-1))is L else C.get((D,E-1));J=B if C.get((D,E+1))is L else C.get((D,E+1));K=B if C.get((D+1,E))is L else C.get((D+1,E));A(H,I,J,K);return x([H[0]==F or H[1]==G or H==B,I[0]==F or I[1]==G or I==B,J[0]==F or J[1]==G or J==B,K[0]==F or K[1]==G or K==B])
def X(board,column,row):
	E=row;D=column;C=board;A=[L,L,L,L]
	if C.get((D-1,E))==B:A[0]=P
	if C.get((D,E-1))==B:A[1]=P
	if C.get((D,E+1))==B:A[2]=P
	if C.get((D+1,E))==B:A[3]=P
	return A
def s(board,col,row):
	A=0;B=X(board,col,row)
	if B.count(L)==2:A=1
	elif B.count(L)==3:A=2
	elif B.count(L)==4:A=4
	else:A=0
	return A
def t():A('[$] HELP');A('[#] Colors:\n    RED : r\n    GREEN : g\n    BLUE : b\n    YELLOW = y\n    CYAN = c\n    PURPLE = p');A('[#] Patterns:\n    TURTLE : 1\n    LIZARD : 2\n    FLOWER : 3\n    FEATHER : 4\n    BIRD : 5 ')
if __name__=='__main__':
	Y=2;u=P;H=n();H[(4,4)]=M.choice(U),M.choice(V);N=l();C=1;M.shuffle(N);J=N[:O(N)//2];K=N[O(N)//2:];M.shuffle(J);M.shuffle(K);R=0;S=0
	while u:
		os.system('cls');E=[];D=0;A(O(J));A(O(K));A(K==J)
		if C==1:E=J;D=R
		elif C==2:E=K;D=S
		A('[#] Lattice Hawaii Python Version');A('\n');A('[!] Board row/col reference (spots with $ are suns)');q(H);A('[!] The board');p(H);A(f"[#] Player {C}'s Turn\n");A('Your current tiles: ');o(E[:5]);A('You have {} tiles left'.format(O(E)));A(f"\nYou have {D} points");F=T("[I] Enter the row and column you'd like to place a tile on (eg: 0,0 or 4,4)>> ");G=T('[I] Enter a tile to place down (eg: r,3 = red flower | type ?,? to see options | type x,x to skip to next player) >> ');F=y((int(A)for A in F.split(',')));G=y((A for A in G.split(',')));A(F,G)
		if G==('?','?'):t();T('Press enter to continue...')
		if G==('x','x'):
			A('Skipping!');I.sleep(4)
			if C==1:R=D;J=E
			elif C==2:S=D;K=E
			if C+1>Y:C=1
			else:C+=1
		if G not in E[:5]:A("You don't have that piece!");I.sleep(4);continue
		if not H[F]==B:A("There's already a piece there!");I.sleep(4);continue
		if x(X(H,*F)):A("Can't place in an empty spot!");I.sleep(4);continue
		if r(H,*G,*F):
			A('Placed!');H[F]=G;E.remove(G);D+=s(H,*F)
			if F in W:D+=2
			if D>2:
				v=T('You have enough points to go again! Take another turn: y/n >>')
				if v==z:D-=2;continue
				else:0
			else:A("You don't have enough points to go again!")
			I.sleep(4)
			if C==1:R=D;J=E
			elif C==2:S=D;K=E
			if C+1>Y:C=1
			else:C+=1
		else:A("Can't place that there!");I.sleep(5)
