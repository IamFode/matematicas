function [y] = energy(x)
%ENERGY Computes the energy of a signal.
%  y = ENERGY(x) returns the energy of x.
%  The energy computed as the sum of the 
%  square of the elements of x.

%   See also CUMENERGY.

y = norm(x)^2;