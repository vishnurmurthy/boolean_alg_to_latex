# Scripts, Lectures, Files

boolean_alg_to_latex:
Short script to make worded boolean language into latex format

If anyone is using Latex and does not like typing out latex commands, I spent ~20 min making a short python script to translate "English boolean" language to latex format.

It can be found here: https://github.com/vishnurmurthy/boolean_alg_to_latex/blob/master/boolean_translate.py

So something like:
((p and q) and not r) or (p implies r and q implies r) or r

Becomes:
( ( \textit{p} \wedge \textit{q} ) \wedge \neg \textit{r} ) \vee ( \textit{p} \rightarrow \textit{r} \wedge \textit{q} \rightarrow \textit{r} ) \vee \textit{r}

All you have to do is put in your variables and the expression(s) you want to translate.
