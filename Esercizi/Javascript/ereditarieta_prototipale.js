Persona = function(nome, annoNascita)
{
    this.getNome = function(){return nome;};
    this.getAnnoNascita = function(){return annoNascita;};
    this.toString = function(){return this.getNome() + " è nata nel " + this.getAnnoNascita(); };
}

Studente = function(nome, annoNascita, matricola)
{
    this.getNome = function(){return nome;};
    this.getAnnoNascita = function(){return annoNascita;};
    this.getMatricola = function(){return matricola; };
    this.toString = function(){return this.getNome() + " è nata nel " + this.getAnnoNascita() + " matricola numero: " + this.getMatricola() };
}


// definisco una persona prototipo
personaPrototipo = new Persona("Pippo", 1900);

Studente.prototype = personaPrototipo; 
Studente.prototype.constructor = Studente; 


// --------------------- REFACTORING ------------------------------------ //

Persona = function(nome, annoNascita)
{
    this.getNome = function(){return nome;};
    this.getAnnoNascita = function(){return annoNascita;};
    this.toString = function(){return this.getNome() + " è nata nel " + this.getAnnoNascita(); };
}

Studente = function(nome, annoNascita, matricola)
{
	Persona.call(this, nome, annoNascita);
    this.getMatricola = function(){return matricola; };
    this.toString = function(){return Studente.prototype.toString.call(this) + " matricola numero: " + this.getMatricola() };
}


// definisco una persona prototipo
personaPrototipo = new Persona("Pippo", 1900);

Studente.prototype = personaPrototipo; 
Studente.prototype.constructor = Studente; 