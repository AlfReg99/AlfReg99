# Repository Tesi
All'interno di questa repository sono stati inseriti tutti i file utilizzati nel lavoro di tesi.

### Tool Utilizzati
Durante il processo di sviluppo della tesi sono stati utilizzati due tool di valutazione automatica dei controlli di sicurezza dei sistemi.

#### CIS CAT Lite
Il primo tool utilizzato è stato CIS Configuration Assessment Tool (CAT) Lite, sviluppato dal Center for Internet Security. È stata realizzata 
una cartella apposita all'interno della quale sono stati inseriti tutta una serie di file PDF associati ai CIS Benchmarks relativi a differenti
sistemi target (es. Windows 10, MacOS, Linux Ubuntu).
###### REPORT CIS CAT Lite
Con il lavoro di tesi svolto, il sistema target scelto per l'esecuzione del tool è stato Windows 10. All'interno di questa repository è stato 
inserito l'intero report in formato HTML generato da CIS CAT Lite.

#### Chef InSpec
Il secondo tool utilizzato è stato Chef InSpec, di proprietà della Chef Software, Inc. Poichè Chef InSpec fa uso sia degli Security Technical Implementation Guides
(STIGs) sia dei CIS Benchmarks, è stata realizzata una seconda cartella all'interno della quale sono stati inseriti tutta una serie di STIGs e di CIS Benchmark
utilizzabili direttamente tramite Chef InSpec.
###### REPORT Chef InSpec
Con il lavoro di tesi svolto, il sistema target scelto per l'esecuzione del tool è stato Windows 10. All'interno di questa repository è stato 
inserito l'intero report sia in formato HTML sia in formato JSON generato da Chef InSpec.

### Script
Un ulteriore lavoro svolto è stata la realizzazione di uno script in linguaggio python. L'obiettivo di tale script è stato quello di prelevare,
in maniera del tutto automatica, tutta una serie di dati relativi ad ogni singolo CIS Benchmark a partire direttamente dal report in formato HTML generato da CIS CAT Lite. I dati prelevati 
appartegono alle seguenti sezioni:
- Famiglia
- Gruppo 
- CIS Benchmark
- Descrizione
- CIS Controls (V7.0 e V8.0)
- CIS Subcontrols (V7.0 e V8.0)
- CIS Implementation Group (IG)
- Risultato Atteso
- Risultato Ottenuto
- Esito

Il file associato allo script è stato inserito all'interno di questa repository con il nome di "main.py". È stato realizzato un secondo file Python, ovvero "Data.py"
all'interno del quale sono stati inseriti tutti i nominativi delle Famiglie e dei Gruppi individuati all'interno del report in modo tale da semplificare l'associazione
di ogni CIS Benchmark con la Famiglia e con il Gruppo.

###### Tabella Excel Report
Inoltre, il secondo obiettivo dello script è stato quello di storicizzare in maniera automatica tutti i dati all'interno di una tabella excel. All'interno di
questa repository è stata inserita la tabella excel di cui abbiamo appena parlato. Il file relativo a tale tabella è "report.xlsx".
###### Tabella Excel Mapping
All'interno di questa repositori è stata inserita un'ulteriore tabella Excel contenente il mapping tra i controlli utilizzati da Chef InSpec con i CIS Benchmarks, i 
CIS Controls ed i CIS Subcontrols del CIS. Questo mapping è stato realizzato prendendo in considerazione la tabella Excel generata automaticamente dallo script precedente.
Il nome del file contente tala tabella Excel è "Tabella_Chef_InSpec.xlsx".
