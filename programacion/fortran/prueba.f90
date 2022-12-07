program cadenas
implicit none

character(10) :: a
character(50) :: b
character(100) :: x

a = 'Hola mundo'
b = 'Hola soy fernando'
x = a // b

print*,trim(x)
end program
