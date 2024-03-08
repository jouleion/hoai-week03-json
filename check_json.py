

# @Students: this code is intentionally unreadable#


Y='frame';Q='label';N='sep';M='time';D=exit;B=print
import json as V,time as E,datetime as Z,cv2 as F,numpy as H,sys,os as I;R=f"{I.path.dirname(I.path.realpath(__file__))}/digits.json"
if sys.argv.__len__()>1:R=sys.argv[1]
if __name__=='__main__':
	B('This program will try to read your json file and then visualize it. You can see the annotations you made on screen and correct them if need by indicating the correct label during the frame which is incorrect. To correct a separation between digits, press s.')
	try:
		with open(R,'r')as a:A=V.load(a)
	except:B(f'Could not read the json file from {I.getcwd()}/{R}. The visualizer expects a file called digits.json in the same folder. You can also give the name of the json file as an argument for the program. The json file should contain one or more frames of data from the patch. The datastructure of the json file should be [{M: timestamp, "label": int, "sep": bool, "frame": pixel array }, ...].');D(1)
	c=1700000000
	try:c=A[0][M];l=Z.datetime.fromtimestamp(A[0][M]).strftime('%Y-%m-%d %H:%M:%S.%f')
	except:B("Could not read timestamp correctly. Each datapoint should contain an entry named 'time', in which the unix timestamp of the data collection is recorded.");D(1)
	for S in A:
		try:d=int(S[Q])
		except:B("Could not read label correctly. Each datapoint should contain an entry named 'label', in which the label of the collected datapoint is recorded.");D(1)
		try:d=S[N]
		except:B("Could not read sep correctly. Each datapoint should contain an entry named 'sep', which is True on the first datapoint of each new digit. It allows us to separate two datacollections of the same digit one after another");D(1)
		try:W=S[Y]
		except:B("Could not read frame correctly. Each datapoint should contain an entry named 'frame', which contains the data provided by the patch.");D(1)
		if W.__len__()!=27:B('The frame should have exactly 27 rows');D(1)
		if W[0].__len__()!=19:B('The frame should have exactly 19 columns');D(1)
	O,P=27,19;T=H.zeros((O,P));J=T.copy();m=False;e=A[0][M];X=E.time()
	while True:
		X=E.time();J=H.zeros((O,P))
		for G in range(A.__len__()):
			while not E.time()-X>A[G][M]-e:E.sleep(.05)
			if A[G][N]:J=H.zeros((O,P))
			T=A[G][Y];J=H.maximum(J,T);U=F.resize(J,(O*10,P*10));f=10,30;g=F.FONT_HERSHEY_SIMPLEX;h=1;i=255,255,255;j=2;U=F.putText(U,f"{A[G][Q]}",f,g,h,i,j,F.LINE_AA);F.imshow('image',U.astype(H.uint8));C=F.waitKey(1)
			if C=='-1':C=''
			else:C=chr(C&255)
			if C=='q':
				with open(f"{I.path.dirname(I.path.realpath(__file__))}/TSP_recording_{E.strftime('%H_%M_%S',E.localtime())}",'w')as k:V.dump(A,k,indent=0)
				D(0)
			if C>='0'and C<='9':
				B(f"\nChanging the following frames to {C}:");K=L=G
				while L>=0 and not A[L][N]:A[L][Q]=C;B(f"{L} ",end='');L-=1
				while K<A.__len__()and not A[K][N]:A[K][Q]=C;B(f"{K} ",end='');K+=1
			if C=='s':B('Separator changed! This cannot be undone.');A[G][N]=True