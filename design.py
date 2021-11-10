n = int(input('enter_length    : '))
m = int(input('enter_width     : '))
name = input('enter_your_name : ')


class body():
     def upper(m):

          for i in range(1,int((n-1)/2)+1):
               if int((m-(3*(1+2*(i-1))))/2) >0:
                    print(("-"*int((m-(3*(1+2*(i-1))))/2)),
                          (".|.")*(1+2*(i-1)),
                          ("-"*int((m-(3*(1+2*(i-1))))/2)),
                          sep='')
               else:
                    pass


     def middle(m):
          
          if m%2==0 and len(name)%2==0:
               print("-"*int((m-len(name))/2),
                     name,
                     "-"*int(((m-len(name))/2)-1),
                     sep='')
               
          elif m%2!=0 and len(name)%2==0:
               print("-"*int((m-len(name))/2),
                     name,
                     "-"*int(((m-len(name))/2)+1),
                     sep='')
          else:
               print("-"*int((m-len(name))/2),
                     name,
                     "-"*int(((m-len(name))/2)),
                     sep='')
               

     def lower(m,n):

          if n%2==0:
               n=n-1
          else:
               pass
          
          for i in range(1,int((n-1)/2)+1):
               if int((m-(3*((n-2)-2*(i-1))))/2)>0:
                    print(("-"*int((m-(3*((n-2)-2*(i-1))))/2)),
                          (".|.")*((n-2)-2*(i-1)),
                          ("-"*int((m-(3*((n-2)-2*(i-1))))/2)),
                          sep='')
               else:
                    pass
          
body.upper(m)
body.middle(m)
body.lower(m,n)
