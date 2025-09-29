from pyscript import display, document

def sample_function(e):
    name = document.getElementById('theName').value
    age = document.getElementById('theAge').value
    school = document.getElementById('theSchool').value


    document.getElementById('output1').innerHTML = "  "
    document.getElementById('output2').innerHTML = "  "
    document.getElementById('output3').innerHTML = "  "
    document.getElementById('output4').innerHTML = "  "

    display(f'   Name: {name}', target='output1')
    display(f'   Age: {age}', target='output2')
    display(f'   School: {school}', target='output3')
    display(f'   {name} is {age} years old was a student at \'{school}\', now currently studying at O.B. Montessori \\ Greenhills', target='output4')