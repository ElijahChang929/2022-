%%
clc;
close all;
clear;
I = imread('4.png'); 
R2 = I(:,:,1);
G2 = I(:,:,2);  
B2 = I(:,:,3);  

R=R2(1284,:);
G=G2(1284,:);
B=B2(1284,:);



lamda=[];
I=[];
L=0.15;
d=1*10^(-3)/500;

for i=800:1600
    G1(i-799)=G(i);
    B1(i-799)=B(i);
    R1(i-799)=R(i);
end

[m1,x1]=max(G1);
[m2,x2]=max(B1);
[m3,x3]=max(R1);
x0=(x1+x2+x3)/3+600;
x0=round(x0);
    
    
    
for i=x0:2800
    lamda(i-x0+1)=d/sqrt(1+(L*2.107334e+04/(i-x0))^2);
end
for i=x0:2800
    A=[];
    A(1)=B(i);
    A(2)=G(i);
    A(3)=R(i);
    M=max(A);
    m=min(A);
    I(i-x0+1)=(M+m)/2;
end

s=size(lamda);
y=0;
for i=1:s(1,2)
    if lamda(i)<300*10^(-9)
        y=y+1;
    elseif lamda(i)>=300*10^(-9)&&lamda(i)<=900*10^(-9)
        lamda0(i-y)=lamda(i);
        I0(i-y)=I(i);
    end
end
I0=smooth(I0);
lamda0 = lamda0*1e9;
plot(lamda0,I0);
set(gca,'yticklabel',[]);
ylabel('相对光强')
xlabel('波长（nm）')
title('白炽灯光谱');