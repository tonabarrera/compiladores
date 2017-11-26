%{
       #include <stdio.h>  /* For printf, etc. */
       #include <math.h>   /* For pow, used in the grammar.  */
       int yylex (void);
       void yyerror (char const *);
%}

%define api.value.type union /* Generate YYSTYPE from these types:  */
%token <double>  NUM         /* Simple double precision number.  */
%token <double> VAR FNCT FUNCTION    /* Symbol table pointer: variable and function.  */
%type  <double>  expr
%type  <double>  asig stmt stmtlist

%right '='
%left OR
%left AND
%left GT GE LT LE EQ NE
%left '-' '+'
%left '*' '/'
%left NEG NOT /* negation--unary minus */
%right '^'      /* exponentiation */

%% /* The grammar follows.  */
lista:
  %empty
  | lista '\n'
  | lista defunc '\n'
  | lista asig '\n'
  | lista stmt
  | lista expr '\n'     { printf ("%.10g\n", $2); }
  | lista error '\n'    { yyerrok; }
  ;

stmt: expr
    | '{' stmtlist '}' { $$ = $2; }
    ;

stmtlist: %empty
        | stmtlist '\n'
        | stmtlist stmt
          ;

expr:
  NUM                       { $$ = $1; printf("Vi un numero\n"); }
  | VAR                     { $$ = $1; printf("Vi una variable\n"); }
  | asig
  | FNCT '(' expr ')'       { $$ = $3; printf("Vi una funcion\n"); }
  | expr '+' expr           { $$ = $1 + $3; }
  | expr '-' expr           { $$ = $1 - $3; }
  | expr '*' expr           { $$ = $1 * $3; }
  | expr '/' expr           { $$ = $1 / $3; }
  | expr '^' expr           { $$ = pow ($1, $3); }
  | '-' expr  %prec NEG     { $$ = -$2; }
  | expr GT expr            { $$ = $1 > $3; }
  | expr GE expr            { $$ = $1 >= $3; }
  | expr LT expr            { $$ = $1 < $3; }
  | expr LE expr            { $$ = $1 <= $3; }
  | expr EQ expr            { $$ = $1 == $3; }
  | expr NE expr            { $$ = $1 != $3; }
  | expr AND expr           { $$ = $1 && $3; }
  | expr OR expr            { $$ = $1 || $3; }
  | NOT expr                { $$ = !$2; }
  ;

asig:
  VAR '=' expr      { $$ = $3; printf("Vi una asignacion\n"); }
  ;


defunc: FUNCTION procnombre { printf("FUNCT"); }
        '('' '')' stmt { printf("stmt"); }
        ;

procnombre: VAR
            ;

/* End of grammar.  */
%%

/* Called by yyparse on error.  */
     void
     yyerror (char const *s)
     {
       fprintf (stderr, "%s\n", s);
     }

     int
     main (int argc, char const* argv[])
     {
       return yyparse ();
     }
