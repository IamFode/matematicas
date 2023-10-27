for i=1:long-10
    open=dat(i:i+9,3);
    close=dat(i:i+9,6);
    intervalos=linspace(A(i,1),A(i,2),11);
    for j=i:i+9
        maximo=max(open(j-i+1),close(j-i+1));
        minimo=min(open(j-i+1),close(j-i+1));
        for k=1:10
            if minimo<=intervalos(k+1) && intervalos(k)<maximo
                Matriz{i}(k,j-i+1)=1;
            else
                Matriz{i}(k,j-i+1)=0;
        end
    end
end
Matriz{i}=flipud(Matriz{i});
end