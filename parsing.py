import sys
import os
import subprocess
from git import Repo

def own_title(L):
        s = []
        previous_is_cased = False
        for c in L:
            if c.islower():
               if not previous_is_cased:
                  c = c.upper()
               previous_is_cased = True
            elif c.isupper():
               previous_is_cased = True
            else:
               previous_is_cased = False
            s.append(c)
        return ''.join(s)

def git_push(git_path,message,file):
    try:
        repo = Repo(git_path)
        repo.config_writer().set_value("user", "name", "Tanguy PEMEJA").release()
        repo.config_writer().set_value("user", "email", "tpemeja@enseirb-matmeca.fr").release()
        repo.git.pull()
        repo.git.add(file)
        repo.index.commit(message)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

dico = {
    'Link':
    [')',
    ' -->',
    ""],
    'Title':
    ['<div data-cy="question-title" class="css-v3d350">',
    '</div>',
    ""],
     'Problem':
     ['question-content__JfgR"><div><p>',
     '</div></div>',
     ""
     ]
     }

list_file = sys.argv

directory_name = "/Basic Challenge/"

if("-c" in list_file):
    dico['Title'] = ['<i title="Coding Question" class="fa fa-file-code-o content-icon" aria-hidden="true"></i> &nbsp;</span>','</div>',""]
    dico['Problem'] = ['<div class="question-area"><div class="question-detail"><div class="question-description__3U1T"><div>','</div></div>',""]
    list_file.remove("-c")
    directory_name = "/Daily Challenge/"

for f in list_file[1:]:
    print("\n File : {}".format(f))
    f = open(f, "r", encoding="utf8")
    text= f.read()

    for key in dico.keys():
        print(key)
        i_beg = text.index(dico[key][0]) + len(dico[key][0])
        text = text[i_beg:]

        i_end = text.index(dico[key][1])
        dico[key][2] = text[:i_end]

        text = text[i_end:]

    # define the name of the directory to be created
    if(directory_name == "/Basic Challenge/"):
        title = own_title(dico['Title'][2]).replace(" ","")
        ind = title.index(".")
        path = os.getcwd()+directory_name+title[:ind]+" - "+title[ind+1:]
    else:
        path = os.getcwd()+directory_name+own_title(dico['Title'][2]).replace(" ","")
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory {} failed or already exist".format(path))

    with open(path+"/README.md", "w") as f:
        f.write('# [{}]({})\n'.format(dico['Title'][2],dico['Link'][2]))
        f.write(dico['Problem'][2])
        f.write('\n\n#### Solutions:\n')
        f.write('- [ ] **C :** [solution.c](solution.c)\n')
        f.write('- [ ] **Python3 :** [solution.py](solution.py)\n')

    git_push(os.getcwd()+"/.git","Add README.md",path+"/README.md")



