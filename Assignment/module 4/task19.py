#How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets. 

'''
    First try clause is executed i.e. the code between try and except clause. 
    If there is no exception, then only try clause will run, except clause will not get executed. 
    If any exception occurs, the try clause will be skipped and except clause will run.
'''
'''
    try:
       # Some Code.... 

except:
       # optional block
       # Handling of exception (if required)

else:
       # execute if no exception

finally:
      # Some code .....(always executed)
'''
