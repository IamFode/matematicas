function y=medmov(x,k)
n=length(x);
y=zeros(n-k+1,1);
y(1)=sum(x(1:k))/k;
for i=2:n-k+1
y(i)=(k*y(i-1)-x(i-1)+x(i-1+k))/k;
end