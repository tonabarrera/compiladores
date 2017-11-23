%{
       #include <stdio.h>  /* For printf, etc. */
       #include <math.h>   /* For pow, used in the grammar.  */
       int yylex (void);
       void yyerror (char const *);
%}

%define api.value.type union /* Generate YYSTYPE from these types:  */
%token <double>  NUM         /* Simple double precision number.  */
%token <double> VAR FNCT    /* Symbol table pointer: variable and function.  */
%type  <double>  exp

%precedence '='
%left '-' '+'
%left '*' '/'
%precedence NEG /* negation--unary minus */
%right '^'      /* exponentiation */

%% /* The grammar follows.  */
input:
  %empty
  | input line
  ;

line:
  '\n'
  | exp '\n'   { printf ("%.10g\n", $1); }
  | error '\n' { yyerrok;                }
  ;

exp:
  NUM                  { $$ = $1; printf("Vi un numero\n");}
  | VAR                { $$ = $1; printf("Vi una variable\n");}
  | VAR '=' exp        { $$ = $3; printf("Vi una asignacion\n");}
  | FNCT '(' exp ')'   { $$ = $3; printf("Vi una funcion\n"); }
  | exp '+' exp        { $$ = $1 + $3;                    }
  | exp '-' exp        { $$ = $1 - $3;                    }
  | exp '*' exp        { $$ = $1 * $3;                    }
  | exp '/' exp        { $$ = $1 / $3;                    }
  | '-' exp  %prec NEG { $$ = -$2;                        }
  | exp '^' exp        { $$ = pow ($1, $3);               }
  | '(' exp ')'        { $$ = $2;                         }
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
