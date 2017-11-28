%{
    #include"hoc.tab.h"
    #include <stdlib.h>
%}

%%

"func" {return FUNC;}
"proc" {return PROC;}
[a-z]+ {return VAR;}

[0-9]+ {yylval.NUM = (double) atoi(yytext); return NUM;}
'-' {return NEG;}
[ \t]+ 
. {return *yytext;}
\n {return '\n';}

%%
