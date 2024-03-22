function [y] = cumenergy(x)
%CUMENERGY Computes the normalized cumulative energy profile.
%  y = CUMENERGY(x) creates a vector y with the normalized
%  cumulative energy profile of vector x.

%   See also ENERGY.

y = cumsum(x.^2)/(norm(x)^2);