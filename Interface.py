# -*- coding:utf-8 -*

from tkinter import *
from tkinter import messagebox
from Student import Student
from Teacher import *
from CollegeSubjects import *
from DatabaseManager import DatabaseManager

DatabaseManager = DatabaseManager("academic.db")

attributesTableStudents = ["name", "gender", "date_of_birth", "rg", "id"]
attributesTableTeachers = ["name", "gender", "academic_degree", "date_of_birth", "rg", "id"]
attributesTableCollegeSubjects = ["name", "course", "id"]
attributesTableNotes = ["id_teacher", "id_college_subject", "note1", "note2", "id"]

tableAluno = "students"
tableProfessor = "teachers"
tableDisciplina = "college_subjects"
tableNotes = "notes"

objetoAluno = Student(None, None, DatabaseManager, None, None, None, tableAluno)
objetoProfessor = Teacher(None, None, DatabaseManager, None, None, None, tableProfessor, None)
objetoDisciplina = CollegeSubjects(None, None, None, DatabaseManager, tableDisciplina)



def inicializaObjeto(nome):
    objeto = None
    
    if nome.lower() == "aluno":
        objeto = Student(None, None, DatabaseManager, None, None, None, tableAluno)
        
    elif nome.lower() == "professor":
        objeto = Teacher(None, None, DatabaseManager, None, None, None, tableProfessor, None)

    elif nome.lower() == "disciplina":
        objetoDisciplina = CollegeSubjects(None, None, None, DatabaseManager, tableDisciplina)

    return objeto

def exibirString(nome):
    
    if nome.lower() == "aluno":
        return "Alunos"
        
    elif nome.lower() == "professor":
        return "Professores"

    elif nome.lower() == "disciplina":
        return "Disciplinas"
        

def criarTitulo(janela, texto, fonte, cor):
    
     titulo = Label(janela,
                       text=texto,
                       font=fonte,
                       bg=cor,
                       fg="white",
                       width="600",
                       height="1").pack()
     return titulo

def criarLabel(janela, texto, abscissa, ordenada):
    label = Label(janela, text=texto)
    label.place(x=abscissa, y=ordenada)
    return label

def desenharJanelaFilha(largura, altura, tam):
    janelaFilha = Toplevel(width=largura, height=altura)
    janelaFilha.geometry(tam)
    
    return janelaFilha

def dadosVazios(tam):
    if tam <= 0:
        messagebox.showinfo("Aviso", "Não há dados cadastrados no banco!")
        return True
    else:
        return False

# Cria a classe janela que herda da biblioteca tkinter a classe Frame
class Janela(Frame):
    def __init__(self, master=None):
        self.__master = master
        # parâmetros a serem enviados pela classe Frame
        Frame.__init__(self, master)
        # instanciamos o novo objeto janela que será criado
        self.janelaPrincipal()

    # método que cria o objeto janela filha
    def janelaPrincipal(self):
        self.master.title("Sistema Acadêmico")
        self.master.geometry("600x400")

        titulo = Label(
            text="Menu Principal",
            font=("Arial Bold", 16),
            bg="grey",
            fg="white",
            width="600",
            height="1")
        titulo.pack()

        # instanciamos o menu
        self.menubar = Menu(self)

        # criamos o objeto para o primeiro item do menu
        menu = Menu(self.menubar, tearoff=0)
        # adicionamos a opção cadastro no menu
        self.menubar.add_cascade(label="Opções", menu=menu)

        # adicionamos os subitens da opção cadastro
        menu.add_command(label="Aluno", command=CRUDAluno.tela)
        menu.add_command(label="Professor", command=CRUDProfessor.tela)
        menu.add_command(label="Disciplina", command=CRUDisciplinas.tela)
        menu.add_command(label="Notas", command=CRUDNotas.tela)
        menu.add_separator()
        menu.add_command(label="Sair", command=self.__master.quit)

        menu = Menu(self.menubar, tearoff=0)
        # adicionamos a opção relatório no menu
        #self.menubar.add_cascade(label="Relatório", menu=menu)

        menu = Menu(self.menubar, tearoff=0)
        # adicionamos a opção sair no menu
        #self.menubar.add_cascade(label="Notas", menu=menu)

        self.master.config(menu=self.menubar)


# cria a classe do formulário CRUD de alunos
class CRUDAluno(Janela):
    @staticmethod
    def __init__(self, master):
        super().__init__(master)

    @staticmethod
    def tela():
        dados = objetoAluno.listAll()
        tamanho = len(dados)

        contaID = tamanho + 1
        sexo = ["Não informado", "Masculino", "Feminino"]

        janelaFilhaAluno = desenharJanelaFilha(100, 100, "600x400+120+120")

        listaSexo = StringVar(janelaFilhaAluno)
        listaSexo.set(sexo[1])
        
        titulo = criarTitulo(janelaFilhaAluno, "Cadastro de Alunos", ("Arial Bold", 16), "blue")

        lblId = criarLabel(janelaFilhaAluno, "Alunos Cadastrados: ", 20, 30)
        
        exibeDados = Listbox(janelaFilhaAluno, width=80, height=10)
        exibeDados.place(x=20, y=50)

        for i in range(tamanho):
            exibeDados.insert(END, dados[i][1])

        lblId = criarLabel(janelaFilhaAluno, "ID: ", 20, 230)

        fldlId = criarLabel(janelaFilhaAluno, contaID, 50, 230)

        lblNome = criarLabel(janelaFilhaAluno, "Nome", 80, 230)
        
        fldNome = Entry(janelaFilhaAluno, width=60)
        fldNome.place(x=130, y=230)

        lblSexo = criarLabel(janelaFilhaAluno, "Sexo", 20, 270)
        
        fldSexo = OptionMenu(janelaFilhaAluno, listaSexo, *sexo)
        fldSexo.place(x=70, y=270)

        lblDataNasc = criarLabel(janelaFilhaAluno, "Data Nascimento: ", 210, 270)

        fldDataNasc = Entry(janelaFilhaAluno, width=10)
        fldDataNasc.place(x=320, y=270)


        lblRg = criarLabel(janelaFilhaAluno, "RG: ", 400, 270)
        
        fldRg = Entry(janelaFilhaAluno, width=20)
        fldRg.place(x=440, y=270)

        def atualizaDados():
            
            dados = objetoAluno.listAll()
            tamanho = len(dados)
            
            if not dadosVazios(tamanho):
            
                alunos = []

                janelaFilhaAtualiza = desenharJanelaFilha(100, 100, "600x400+120+120")

                for i in range(tamanho):
                    alunos.append(str(dados[i][0]) + " -" + dados[i][1])

                listaAluno = StringVar(janelaFilhaAtualiza)
                listaAluno.set(str(dados[0][0]) + "   -" + dados[0][1])

                titulo = criarTitulo(janelaFilhaAtualiza, "Alterar Dados/Excluir Alunos", ("Arial Bold", 16), "grey")


                lblPesquisa = criarLabel(janelaFilhaAtualiza, "Selecione o(a) Aluno(a):", 20, 40)

                fldPesquisa = OptionMenu(janelaFilhaAtualiza, listaAluno, *alunos)
                fldPesquisa.place(x=160, y=40)

                def pesquisaDados():
                   
                    getId = listaAluno.get()[:2]

                    objetoAluno.setId(getId)
                   
                    aluno = objetoAluno.listAData()
                    
                    getNome = StringVar(janelaFilhaAtualiza, value=aluno[0][1])
                    getSexo = StringVar(janelaFilhaAtualiza, value=aluno[0][2])
                    getDataNasc = StringVar(janelaFilhaAtualiza, value=aluno[0][3])
                    getRg = StringVar(janelaFilhaAtualiza, value=aluno[0][4])

                
                    lblId2 = criarLabel(janelaFilhaAtualiza, "ID:  " + str(aluno[0][0]), 20,90)

    
                    lblNome2 = criarLabel(janelaFilhaAtualiza, "Nome: ", 80, 90)
                    
                    fldNome2 = Entry(janelaFilhaAtualiza, textvariable=getNome)
                    fldNome2.place(x=130, y=90)

    
                    lblSexo2 = criarLabel(janelaFilhaAtualiza, "Sexo: ", 330, 90)
                    
                    fldSexo2 = Entry(janelaFilhaAtualiza, textvariable=getSexo, width=5)
                    fldSexo2.place(x=380, y=90)



                    lblDataNasc2 = criarLabel(janelaFilhaAtualiza, "Data Nascimento: ", 20, 120)

                    
                    fldDataNasc2 = Entry(janelaFilhaAtualiza, textvariable=getDataNasc, width=15)
                    fldDataNasc2.place(x=130, y=120)

                

                    lblRg2 = criarLabel(janelaFilhaAtualiza, "RG: ", 260, 120)

                                        
                    fldRg2 = Entry(janelaFilhaAtualiza, textvariable=getRg)
                    fldRg2.place(x=290, y=120)

                    def alteraDados():
                        
                        novoNome = fldNome2.get()
                        novoSexo = fldSexo2.get()
                        novoDataNasc = fldDataNasc2.get()
                        novoRg = fldRg2.get()

            
                        objetoAluno.update(attributesTableStudents, [novoNome, novoSexo, novoDataNasc, novoRg, getId])
                        messagebox.showinfo("Aviso", "Dados atualizados no banco!")

                    def excluiDados():
                       
                        getId = listaAluno.get()[:2]
                        msg = messagebox.askquestion("Confirmar", "Deseja mesmo excluir estes dados?", icon='warning')
                        if msg == "yes":
                            objetoAluno.setId(getId)
                            objetoAluno.delete()
                            messagebox.showinfo("Aviso", "Dados excluídos no banco!")

                    btnAtualizaDados = Button(janelaFilhaAtualiza, text=' Atualizar ', command=alteraDados)
                    btnAtualizaDados.place(x=100, y=330)

                    btnExcluiDados = Button(janelaFilhaAtualiza, text=' Excluir ', command=excluiDados)
                    btnExcluiDados.place(x=230, y=330)

                btnOk = Button(janelaFilhaAtualiza, text=' OK ', command=pesquisaDados)
                btnOk.place(x=330, y=40)

                btnSair = Button(janelaFilhaAtualiza, text=' Fechar ', command=janelaFilhaAtualiza.destroy)
                btnSair.place(x=360, y=330)

        def salvaDados():
            
            nome = fldNome.get()
            nasc = fldDataNasc.get()
            sexo = listaSexo.get()
            rg = fldRg.get()
            if nome == "":
                messagebox.showinfo("Erro", "Informe um nome!")
            elif sexo == "":
                messagebox.showinfo("Erro", "Informe um sexo!")
            elif nasc == "":
                messagebox.showinfo("Erro", "Informe uma data de nascimento!")
            elif rg == "":
                messagebox.showinfo("Erro", "Informe um número de RG!")
            else:
                objetoAluno.insert([contaID, nome, sexo, nasc, rg])
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")

        btnOk = Button(janelaFilhaAluno, text=' Salvar ', command=salvaDados)
        btnOk.place(x=150, y=330)

        btnAtualiza = Button(janelaFilhaAluno, text=' Atualizar/Excluir ', command=atualizaDados)
        btnAtualiza.place(x=230, y=330)

        btnSair = Button(janelaFilhaAluno, text=' Fechar ', command=janelaFilhaAluno.destroy)
        btnSair.place(x=360, y=330)


# cria a classe do formulário CRUD de professores
class CRUDProfessor(Janela):
    @staticmethod
    def __init__(self, master):
        super().__init__(master)

    @staticmethod
    def tela():
        
        dados = objetoProfessor.listAll()
        tamanho = len(dados)

        contaID = tamanho + 1
        sexo = ["Não informado", "Masculino", "Feminino"]
        titulacao = ["Não informado", "Especialista", "Mestre", "Doutor"]

        janelaFilhaProfessor = desenharJanelaFilha(100, 100, "600x400+120+120")
        
        listaSexo = StringVar(janelaFilhaProfessor)
        listaSexo.set(sexo[0])

        listaTitulacao = StringVar(janelaFilhaProfessor)
        listaTitulacao.set(titulacao[0])

        
        titulo = criarTitulo(janelaFilhaProfessor, "Cadastro de Professores", ("Arial Bold", 16), "green")

        lblId = criarLabel(janelaFilhaProfessor, "Professores Cadastrados: ", 20, 30)
        
        exibeDados = Listbox(janelaFilhaProfessor, width=80, height=10)
        exibeDados.place(x=20, y=50)

        for i in range(tamanho):
            exibeDados.insert(END, dados[i][1])

        lblId = criarLabel(janelaFilhaProfessor, "ID: ", 20, 230)

        fldlId = criarLabel(janelaFilhaProfessor, contaID, 50, 230)

        lblNome = criarLabel(janelaFilhaProfessor, "Nome", 80, 230)
        
        fldNome = Entry(janelaFilhaProfessor, width=60)
        fldNome.place(x=130, y=230)

        lblSexo = criarLabel(janelaFilhaProfessor, "Sexo", 20, 270)
        
        fldSexo = OptionMenu(janelaFilhaProfessor, listaSexo, *sexo)
        fldSexo.place(x=60, y=270)

        lblDataNasc = criarLabel(janelaFilhaProfessor, "Data Nascimento: ", 20, 300)

        fldDataNasc = Entry(janelaFilhaProfessor, width=10)
        fldDataNasc.place(x=120, y=300)

        lblRg = criarLabel(janelaFilhaProfessor, "RG: ", 400, 270)
        fldRg = Entry(janelaFilhaProfessor, width=20)
        fldRg.place(x=440, y=270)


        lblTitulacao = Label(janelaFilhaProfessor, text="Titulação:")
        lblTitulacao.place(x=210, y=270)
        fldTitulacao = OptionMenu(janelaFilhaProfessor, listaTitulacao, *titulacao)
        fldTitulacao.place(x=270, y=270)
    
       
        def atualizaDados():
            
            dados = objetoProfessor.listAll()
            tamanho = len(dados)

            if not dadosVazios(tamanho):
                
                profs = []

                janelaFilhaAtualiza = desenharJanelaFilha(100, 100, "600x400+120+120")

                for i in range(tamanho):
                    profs.append(str(dados[i][0]) + " -" + dados[i][1])

                listaProf = StringVar(janelaFilhaAtualiza)
                listaProf.set(str(dados[0][0]) + "   -" + dados[0][1])

                titulo = Label(janelaFilhaAtualiza,
                               text="Alterar Dados/Excluir Professor",
                               font=("Arial Bold", 16),
                               bg="grey",
                               fg="white",
                               width="600",
                               height="1").pack()

                lblPesquisa = Label(janelaFilhaAtualiza, text="Selecione o(a) Professor(a):")
                lblPesquisa.place(x=150, y=70)

                fldPesquisa = OptionMenu(janelaFilhaAtualiza, listaProf, *profs)
                fldPesquisa.place(x=299, y=68)

                def pesquisaDados():
                    
                    getId = listaProf.get()[:2]
                    
                    objetoProfessor.setId(getId)
                    
                    prof = objetoProfessor.listAData()
                    
                    getNome = StringVar(janelaFilhaAtualiza, value=prof[0][1])
                    getSexo = StringVar(janelaFilhaAtualiza, value=prof[0][2])
                    getDataNasc = StringVar(janelaFilhaAtualiza, value=prof[0][3])
                    getRg = StringVar(janelaFilhaAtualiza, value=prof[0][4])
                    getTit = StringVar(janelaFilhaAtualiza, value=prof[0][5])

                    lblId2 = Label(janelaFilhaAtualiza, text="ID:  " + str(prof[0][0]))
                    lblId2.place(x=40, y=150)

                    lblNome2 = Label(janelaFilhaAtualiza, text="Nome: ")
                    lblNome2.place(x=320, y=150)
                    fldNome2 = Entry(janelaFilhaAtualiza, textvariable=getNome, width=30)
                    fldNome2.place(x=370, y=150)

                   
                    lblDataNasc2 = Label(janelaFilhaAtualiza, text="Data Nascimento: ")
                    lblDataNasc2.place(x=40, y=200)
                    fldDataNasc2 = Entry(janelaFilhaAtualiza, textvariable=getDataNasc, width=10)
                    fldDataNasc2.place(x=160, y=200)


                    lblRg2 = Label(janelaFilhaAtualiza, text="RG: ")
                    lblRg2.place(x=320, y=200)
                    fldRg2 = Entry(janelaFilhaAtualiza, textvariable=getRg, width=15)
                    fldRg2.place(x=370, y=200)

                    lblTitulacao2 = Label(janelaFilhaAtualiza, text="Titulação:")
                    lblTitulacao2.place(x=40, y=250)
                    fldTitulacao2 = Entry(janelaFilhaAtualiza,textvariable=getTit, width=15)
                    fldTitulacao2.place(x=160, y=250)

                    lblSexo2 = Label(janelaFilhaAtualiza, text="Sexo: ")
                    lblSexo2.place(x=320, y=250)
                    fldSexo2 = Entry(janelaFilhaAtualiza, textvariable=getSexo, width=15)
                    fldSexo2.place(x=370, y=250)


                    def alteraDados():
                        novoNome = fldNome2.get()
                        novoSexo = fldSexo2.get()
                        novoDataNasc = fldDataNasc2.get()
                        novoRg = fldRg2.get()
                        novoTit = fldTitulacao2.get()
                      
                       
                        objetoProfessor.update(attributesTableTeachers, [novoNome, novoSexo, novoTit, novoDataNasc, novoRg, getId])
                        messagebox.showinfo("Aviso", "Dados atualizados no banco!")

                    def excluiDados():
                        getId = listaProf.get()[:2] 
                       
                        msg = messagebox.askquestion("Confirmar", "Deseja mesmo excluir estes dados?", icon='warning')
                        if msg == "yes":
                            objetoProfessor.setId(getId)
                            objetoProfessor.delete()
                            messagebox.showinfo("Aviso", "Dados excluidos no banco!")

                    btnAtualizaDados = Button(janelaFilhaAtualiza, text=' Atualizar ', command=alteraDados)
                    btnAtualizaDados.place(x=100, y=330)

                    btnExcluiDados = Button(janelaFilhaAtualiza, text=' Excluir ', command=excluiDados)
                    btnExcluiDados.place(x=230, y=330)

                btnOk = Button(janelaFilhaAtualiza, text=' OK ', command=pesquisaDados)
                btnOk.place(x=405, y=70)
               
                btnSair = Button(janelaFilhaAtualiza, text=' Fechar ', command=janelaFilhaAtualiza.destroy)
                btnSair.place(x=360, y=330)

        def salvaDados():
            nome = fldNome.get()
            nasc = fldDataNasc.get()
            sexo = listaSexo.get()
            rg = fldRg.get()
            titulacao = listaTitulacao.get()
            
            if nome == "":
                messagebox.showinfo("Erro", "Informe um nome!")
            elif sexo == "":
                messagebox.showinfo("Erro", "Informe um sexo!")
            elif nasc == "":
                messagebox.showinfo("Erro", "Informe uma data de nascimento!")
            elif rg == "":
                messagebox.showinfo("Erro", "Informe um número de RG!")
            else:
                objetoProfessor.setId(contaID)
                objetoProfessor.setName(nome)
                objetoProfessor.setGender(sexo)
                objetoProfessor.setDateOfBirth(nasc)
                objetoProfessor.setAcademicDegree(titulacao)
                objetoProfessor.setRg(rg)
                objetoProfessor.insert()
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")

        btnOk = Button(janelaFilhaProfessor, text=' Salvar ', command=salvaDados)
        btnOk.place(x=150, y=330)

        btnAtualiza = Button(janelaFilhaProfessor, text=' Atualizar/Excluir ', command=atualizaDados)
        btnAtualiza.place(x=230, y=330)

        btnSair = Button(janelaFilhaProfessor, text=' Fechar ', command=janelaFilhaProfessor.destroy)
        btnSair.place(x=360, y=330)


class CRUDisciplinas(Janela):
    @staticmethod
    def __init__(self, master):
        super().__init__(master)

    @staticmethod
    def tela():
        
        janelaFilha = desenharJanelaFilha(100, 100, "600x400+120+120")
        
        titulo = criarTitulo(janelaFilha, "Cadastro de Alunos", ("Arial Bold", 16), "red")

        lblId = criarLabel(janelaFilha, "Disciplinas Cadastrados:", 20, 30)
        
        exibeDados = Listbox(janelaFilha, width=80, height=5)
        exibeDados.place(x=20, y=50)

        dados = objetoDisciplina.listAll()
        tamanho = len(dados)
        
        for i in range(tamanho):
            exibeDados.insert(END, dados[i][1])

        lblNomeDisciplina = criarLabel(janelaFilha, "Disciplina:", 50, 150)
        
        fldNomeDisciplina = Entry(janelaFilha, width=60)
        fldNomeDisciplina.place(x=130, y=150)
        
        lblNomeCurso = criarLabel(janelaFilha, "Curso:", 50, 180)
        
        fldNomeCurso = Entry(janelaFilha, width=60)
        fldNomeCurso.place(x=130, y=180)

        def salvaDados():
            dados = objetoDisciplina.listAll()
            tamanho = len(dados)
            contaID = tamanho + 1

            disciplina = fldNomeDisciplina.get()
            curso = fldNomeCurso.get()

            if disciplina == "":
                messagebox.showinfo("Erro", "Informe uma disciplina!")
            else:
                objetoDisciplina.insert([contaID, disciplina, curso])
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")

        btnOk = Button(janelaFilha, text=' Salvar ', command=salvaDados)
        btnOk.place(x=150, y=330)

        btnSair = Button(janelaFilha, text=' Fechar ', command=janelaFilha.destroy)
        btnSair.place(x=360, y=330)


        def atualizaDados():
            
            dados = objetoDisciplina.listAll()
            tamanho = len(dados)
            
            if not dadosVazios(tamanho):
            
                disciplinas = []

                janelaFilhaAtualiza = desenharJanelaFilha(100, 100, "600x400+120+120")

                for i in range(tamanho):
                    disciplinas.append(str(dados[i][0]) + " -" + dados[i][1])

                lista = StringVar(janelaFilhaAtualiza)
                lista.set(str(dados[0][0]) + "   -" + dados[0][1])

                titulo = criarTitulo(janelaFilhaAtualiza, "Alterar Dados/Excluir Disciplinas", ("Arial Bold", 16), "grey")


                lblPesquisa = criarLabel(janelaFilhaAtualiza, "Selecione a Disciplina(a):", 20, 40)

                fldPesquisa = OptionMenu(janelaFilhaAtualiza, lista, *disciplinas)
                fldPesquisa.place(x=160, y=40)

                def pesquisaDados():
                   
                    getId = lista.get()[:2]

                    objetoDisciplina.setId(getId)
                   
                    disciplina = objetoDisciplina.listAData()
                    
                    getDisciplina = StringVar(janelaFilhaAtualiza, value=disciplina[0][1])
                    getCurso = StringVar(janelaFilhaAtualiza, value=disciplina[0][2])
                    
                
                    labelId = criarLabel(janelaFilhaAtualiza, "ID:  " + str(disciplina[0][0]), 20,90)
    
                    labelDisciplina = criarLabel(janelaFilhaAtualiza, "Nome: ", 80, 90)
                    
                    entradaDisciplina = Entry(janelaFilhaAtualiza, textvariable=getDisciplina)
                    entradaDisciplina.place(x=130, y=90)

    
                    labelCurso = criarLabel(janelaFilhaAtualiza, "Curso: ", 330, 90)
                    
                    entradaCurso = Entry(janelaFilhaAtualiza, textvariable=getCurso, width=5)
                    entradaCurso.place(x=380, y=90)


                    def alteraDados():
                        
                        disciplina = entradaDisciplina.get()
                        curso = entradaCurso.get()
                       
                        objetoDisciplina.update(attributesTableCollegeSubjects, [disciplina, curso, getId])
                        messagebox.showinfo("Aviso", "Dados atualizados no banco!")

                    def excluiDados():
                       
                        getId = lista.get()[:2]
                        msg = messagebox.askquestion("Confirmar", "Deseja mesmo excluir estes dados?", icon='warning')

                        if msg == "yes":
                            objetoDisciplina.setId(getId)
                            objetoDisciplina.delete()
                            messagebox.showinfo("Aviso", "Dados excluídos no banco!")

                    btnAtualizaDados = Button(janelaFilhaAtualiza, text=' Atualizar ', command=alteraDados)
                    btnAtualizaDados.place(x=100, y=330)

                    btnExcluiDados = Button(janelaFilhaAtualiza, text=' Excluir ', command=excluiDados)
                    btnExcluiDados.place(x=230, y=330)

                btnOk = Button(janelaFilhaAtualiza, text=' OK ', command=pesquisaDados)
                btnOk.place(x=330, y=40)

                btnSair = Button(janelaFilhaAtualiza, text=' Fechar ', command=janelaFilhaAtualiza.destroy)
                btnSair.place(x=360, y=330)

        btnAtualiza = Button(janelaFilha, text=' Atualizar/Excluir ', command=atualizaDados)
        btnAtualiza.place(x=230, y=330)

        btnSair = Button(janelaFilha, text=' Fechar ', command=janelaFilha.destroy)
        btnSair.place(x=360, y=330)

class CRUDNotas(Janela):
    @staticmethod
    def __init__(self, master):
        super().__init__(master)

    @staticmethod
    def tela():
        
        janelaFilha = desenharJanelaFilha(100, 100, "600x400+120+120")

        dados = DatabaseManager.listData("notes")
        
        tamanho = len(dados)
        contaID = tamanho + 1

        titulo = criarTitulo(janelaFilha, "Cadastro de Notas do Aluno na Disciplina", ("Arial Bold", 14), "red")

        lblId = criarLabel(janelaFilha, "Notas Cadastradas:", 20, 30)
        
        exibeDados = Listbox(janelaFilha, width=80, height=5)
        exibeDados.place(x=20, y=50)
        
        for i in range(tamanho):
            exibeDados.insert(END, dados[i][1])


        dadosD = objetoDisciplina.listAll()
        
        tamanho = len(dadosD)
        
        disciplinas = ["Selecione"]

        for i in range(tamanho):
            disciplinas.append(str(dadosD[i][0]) + " -" + dadosD[i][1])

        listaD = StringVar(janelaFilha)
        
        if tamanho>0:
            listaD.set(str(dadosD[0][0]) + "   -" + dadosD[0][1])
        else:
            listaD.set(disciplinas[0])


        #lblNomeDisciplina = criarLabel(janelaFilha, "Nome:", 50, 150)
        
        #fldProfs = OptionMenu(janelaFilha, listaD, *disciplinas)
        #fldProfs.place(x=130, y=150)

        
        dados = objetoProfessor.listAll()
        tamanhoProf = len(dados)
        profs = ["Selecione"]

        for i in range(tamanhoProf):
            profs.append(str(dados[i][0]) + " -" + dados[i][1])

        listaProf = StringVar(janelaFilha)
        
        if tamanhoProf >0:
            listaProf.set(str(dados[0][0]) + "   -" + dados[0][1])
        else:
            listaProf.set(profs[0])


        lblProfs = criarLabel(janelaFilha, "Professor:", 50, 180)
        
        fldProfs = OptionMenu(janelaFilha, listaProf, *profs)
        fldProfs.place(x=130, y=180)

        
        dadosAlunos = objetoAluno.listAll()
        tamanhoAlunos = len(dadosAlunos)
        alunos = ["Selecione"]

        for i in range(tamanhoAlunos):
            alunos.append(str(dadosAlunos[i][0]) + " -" + dadosAlunos[i][1])

        listaAlunos = StringVar(janelaFilha)
        
        if tamanhoAlunos > 0:
            listaAlunos.set(str(dadosAlunos[0][0]) + "   - " + dadosAlunos[0][1])
        else:
            listaAlunos.set(alunos[0])
            
    
        lblalunos = criarLabel(janelaFilha, "Aluno:", 50, 210)
        
        fldalunos = OptionMenu(janelaFilha, listaAlunos, *alunos)
        fldalunos.place(x=130, y=210)


        lblnota1 = criarLabel(janelaFilha, "Nota 1:", 50, 240)
        
        fldnota1 = Entry(janelaFilha, width=20)
        fldnota1.place(x=130, y=240)

        lblnota2 = criarLabel(janelaFilha, "Nota 2:", 50, 270)
        
        fldnota2 = Entry(janelaFilha, width=20)
        fldnota2.place(x=130, y=270)

        def salvaDados():
            id_aluno = listaAlunos.get()
            id_prof = listaProf.get()
            id_disciplina = listaD.get()
            nota1 = fldnota1.get()
            nota2 = fldnota2.get()
            
            
            if id_aluno == "":
                messagebox.showinfo("Erro", "Informe um aluno!")
                
            elif id_prof == "":
                messagebox.showinfo("Erro", "Informe um professor!")
                
            elif id_disciplina == "":
                messagebox.showinfo("Erro", "Informe uma disciplina!")
                
            elif nota1 == "" or nota2=="":
                messagebox.showinfo("Erro", "Informe os valores das notas!")

            else:
                DatabaseManager.insert("notes", [contaID, id_aluno, id_prof, id_disciplina, nota1, nota2])
                messagebox.showinfo("Aviso", "Dados inseridos no banco!")
                
        if tamanhoProf > 0 and tamanhoAlunos > 0:
            btnOk = Button(janelaFilha, text=' Salvar ', command=salvaDados)
            btnOk.place(x=150, y=330)
        #else:
            #texto = criarTitulo(janelaFilha, "Cadastre Aluno e Professor!", ("Arial Bold", 12), "red")
        
        btnSair = Button(janelaFilha, text=' Fechar ', command=janelaFilha.destroy)
        btnSair.place(x=360, y=330)

root = Tk() #permite que widgets  sejam usados na aplicação
Janela(root)
root.mainloop()



