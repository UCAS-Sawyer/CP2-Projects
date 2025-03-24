#Sawyer Wood, Debugging notes
import trace
import sys

def trace_calls(frame, event, arg):
    if event == "call": #When smth is called
        print(f"Calling function: {frame.f_code.co_name}")
    elif event == "line": #New line of code
        print(f"Executing line {frame.f_lineno} in {frame.f_code.co_name}")
    elif event == "return": #When return stuff
        print(f"{frame.f_code.co_name} returned {arg}")
    elif event == "exception": #When there are issues(triggered when there is an exception)
        print(f"Exception {frame.f_code.co_name}: {arg}")
    
    return trace_calls

tracer = trace.Trace(count=False, trace=True)

sys.settrace(trace_calls)
def subtract(numone, numtwo):
    return numone - numtwo

def add(numone, numtwo):
    print(subtract(numone, numtwo))
    return numone + numtwo

print(add(5,2))

#tracer.run("add(8,9)")