long=length(dat(:,1));
for i=1:long-10
    mintramo10=min(min(dat(i:i+9,6)),min(dat(i:i+9,3)));
    maxtramo10=max(max(dat(i:i+9,6)),max(dat(i:i+9,3)));
    A(i,1)=mintramo10;
    A(i,2)=maxtramo10;
end