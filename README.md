# app.salomos.com

# Index
* .
   * [README](./README.md)
   * 1
      * [README](./1/README.md)
   * 2
      * [README](./2/README.md)
   * 3
      * [README](./3/README.md)
   * 4
      * [README](./4/README.md)
   * 5
      * [README](./5/README.md)
      * [None](./5/None.md)
      * [1](./5/1.md)
      * [2](./5/2.md)
      * [3](./5/3.md)
      * [4](./5/4.md)
      * [5](./5/5.md)
      * [6](./5/6.md)
      * [7](./5/7.md)
      * [8](./5/8.md)
      * [9](./5/9.md)
      * [10](./5/10.md)
      * [11](./5/11.md)
      * [12](./5/12.md)
      * [13](./5/13.md)
      * [14](./5/14.md)
      * [15](./5/15.md)
      * [16](./5/16.md)
   * 6
      * [1](./6/1.md)
      * [2](./6/2.md)
   * 7
      * [README](./7/README.md)
      * [1](./7/1.md)
      * [2](./7/2.md)
      * [3](./7/3.md)
      * [4](./7/4.md)
      * [5](./7/5.md)
      * [6](./7/6.md)
      * [7](./7/7.md)
      * [8](./7/8.md)
      * [9](./7/9.md)
      * [10](./7/10.md)
      * [11](./7/11.md)
      * [12](./7/12.md)
   * 8
      * [README](./8/README.md)
      * de
         * [1](./8/de/1.md)
         * [2](./8/de/2.md)
         * [3](./8/de/3.md)
         * [4](./8/de/4.md)
         * [5](./8/de/5.md)
         * [6](./8/de/6.md)
         * [7](./8/de/7.md)
         * [8](./8/de/8.md)
         * [9](./8/de/9.md)
         * [10](./8/de/10.md)
         * [11](./8/de/11.md)


## Salomos - smart operations in company. 
Salomos is a voice assistant for the company's operational activities. Works in a flow: SPEECH->NLP->SQL->API providers


![_3f834d89-3ae8-4007-978c-4c518f6d7b11](https://github.com/salomos-com/app/assets/5669657/a8afc4bb-e807-4687-989e-2174de7919ea)




**Salomos**, the voice assistant for smart operations, bridges the gap between spoken language and efficient business processes. 

Let's delve into how this innovative technology can revolutionize operational activities:

1. **Speed and Efficiency**:
   - Voice assistants (VAs) offer rapid communication. Even expert typists are slower than modern VAs at taking down messages.
   - Employees can multitask effectively, as VAs allow hands-free interaction. Responding to urgent messages or sending files becomes seamless without interrupting ongoing tasks.

2. **Popular Use Cases for VAs in Business**:
   - **Embeddable Voice Assistant Technology for Chatbots**: Integrating VAs into chatbots enhances customer interactions. Whether it's answering queries, providing product information, or guiding users through processes, VAs streamline communication and improve user experience¹[1].

3. **Why Businesses Invest in Voice Assistants**:
   - **Speed**: Speaking is faster than typing, making VAs efficient for communication.
   - **Hands-Free**: VAs allow multitasking by keeping both hands free.
   - **Safety**: In workplaces, VAs enhance productivity while ensuring safety.

4. **Smart Operations**:
   - Smart operations leverage digital capabilities to achieve higher performance outcomes. By applying these capabilities at an enterprise scale, businesses can optimize processes and drive profitability²[2].

5. **The Future of Voice Assistants**:
   - As AI and ML continue to evolve, VAs will reshape consumer behavior trends.
   - Conversational user interfaces (CUIs) will play a pivotal role in the future of VAs, enabling seamless interactions across various domains¹[1].

In summary, Salomos represents the fusion of voice technology, NLP, SQL, and API providers, empowering businesses to operate smarter and more efficiently.


## PL


 jak zautomatyzwoać procesy i z perspektywy software developera łatwiej ujarzmić procesy poprzez STT -> NLP -> SQL -> API. Co oznacza, że mogę zautomatyzyowac procesy poprzez realizację zapytań w kolejkach, poprzez zapytanie SQL mam dostęp do źródła danych i usług (poprzez adapter SQL->API)

od technicznej strony trigger może być obsługiwany na poziomie funkcji zaimplementowanej w SQL: 

    CREATE TRIGGER MyTrigger
     AFTER INSERT ON MyTable
     FOR EACH ROW
     BEGIN
     -- Blok kodu SQL
     END;

Albo okresowo w PostgreSQL:

    SELECT cron.schedule('5 minutes', $$UPDATE my_table SET my_column = my_column + 1$$);

Ma to tę zaletę, że można na jednej warstwie aplikacji udokumentować procesy w formie zapytań SQL





 W systemach baz danych SQL triggery są zwykle uruchamiane przez zdarzenia w tabeli (tj. INSERT, UPDATE, DELETE), a nie na podstawie upływu czasu. Jeśli potrzebujesz wykonywać operacje bazodanowe automatycznie w określonych odstępach czasu, powinieneś wykorzystać inne mechanizmy, takie jak zadania zaplanowane (ang. scheduled jobs) lub funkcje cron w systemie operacyjnym.

Niektóre systemy zarządzania bazami danych, takie jak MySQL, PostgreSQL, Oracle, SQL Server, oferują funkcjonalność zaplanowanych zadań, które można wykorzystać do tego celu. Oto jak można to zrealizować w kilku popularnych systemach baz danych:

### 1. **MySQL**

W MySQL możesz użyć mechanizmu zwanego "Event Scheduler". Przykładowo, aby stworzyć zdarzenie, które wykonuje się co minutę:
```sql
CREATE EVENT my_event
ON SCHEDULE EVERY 1 MINUTE
DO
  UPDATE my_table SET my_column = my_column + 1;
```
Możesz również ustawić zdarzenie na wykonanie jednorazowe w przyszłości:
```sql
CREATE EVENT my_once_event
ON SCHEDULE AT '2023-12-31 23:59:00'
DO
  INSERT INTO my_table(name, created_at) VALUES ('Year End', NOW());
```

### 2. **PostgreSQL**

PostgreSQL nie ma wbudowanej funkcji harmonogramowania zadań, ale możesz użyć zewnętrznych narzędzi takich jak `pg_cron` dla serwera PostgreSQL:
```sql
SELECT cron.schedule('5 minutes', $$UPDATE my_table SET my_column = my_column + 1$$);
```

### 3. **Oracle**

W Oracle możesz użyć DBMS_SCHEDULER:
```sql
BEGIN
  DBMS_SCHEDULER.create_job (
    job_name        => 'my_job',
    job_type        => 'PLSQL_BLOCK',
    job_action      => 'BEGIN UPDATE my_table SET my_column = 100; END;',
    start_date      => SYSTIMESTAMP,
    repeat_interval => 'freq=minutely; interval=1',
    end_date        => NULL,
    enabled         => TRUE);
END;
```
Lub dla jednorazowego zadania:
```sql
BEGIN
  DBMS_SCHEDULER.create_job (
    job_name        => 'one_time_job',
    job_type        => 'PLSQL_BLOCK',
    job_action      => 'BEGIN INSERT INTO my_table VALUES (1, ''test'', SYSDATE); END;',
    start_date      => TO_TIMESTAMP_TZ('2023-12-31 23:59:00 TZD', 'YYYY-MM-DD HH24:MI:SS TZR'),
    repeat_interval => NULL,
    enabled         => TRUE);
END;
```

### 4. **Microsoft SQL Server**

W SQL Server korzysta się z SQL Server Agent:
```sql
-- Create a job
EXEC dbo.sp_add_job @job_name = N'MyJob';  

-- Add a job step that contains the command
EXEC sp_add_jobstep @job_name = N'MyJob', @step_name = N'MyStep',  
    @subsystem = N'TSQL',  
    @command = N'UPDATE my_table SET my_column = my_column + 1;',   
    @retry_attempts = 0;

-- Schedule the job to run every minute
EXEC dbo.sp_add_schedule @schedule_name = N'MySchedule', 
    @freq_type = 4, @freq_interval = 1, @freq_subday_type = 4, @freq_subday_interval = 1;
EXEC sp_attach_schedule @job_name = N'MyJob', @schedule_name = N'MySchedule';
  
-- Enable the job
EXEC dbo.sp_update_job @job_name = N'MyJob', @enabled = 1;
```

W przypadku każdego systemu baz danych, ważne jest zrozumienie szczegółów implementacyjnych oraz potencjalnego wpływu na wydajność bazy danych. Zadania zaplanowane działają na poziomie serwera baz danych i są niezależne od aplikacji, co czyni je efektywnym rozwiązaniem do wykonywania operacji cyklicznych.





Triggery są implementowane na poziomie bazy danych i wykonują określone funkcje SQL w odpowiedzi na zdarzenia takie jak INSERT, UPDATE, lub DELETE. Oto kilka aspektów technicznych związanych z triggerami:

1. **Definicja Trigera**: Tworzenie triggera zwykle rozpoczyna się od określenia momentu jego uruchomienia (BEFORE, AFTER, INSTEAD OF) w zależności od operacji (INSERT, UPDATE, DELETE). Na przykład:
   ```sql
   CREATE TRIGGER MyTrigger
   AFTER INSERT ON MyTable
   FOR EACH ROW
   BEGIN
     -- Blok kodu SQL
   END;
   ```

2. **Korzystanie ze starszych i nowych wartości**: W triggerech, które reagują na UPDATE, często można uzyskać dostęp do starych i nowych wartości rekordów korzystając z specjalnych pseudonimów. Na przykład `OLD.col_name` i `NEW.col_name` pozwalają porównać wartości przed i po aktualizacji.

3. **Zakres wykonania**: Triggery mogą być ustawione na wywołanie dla każdego rekordu (`FOR EACH ROW`) lub jednokrotnie dla całej instrukcji (`FOR EACH STATEMENT`), co zależy od systemu zarządzania bazą danych.

4. **Unikanie nieskończonych pętli rekursywnych**: Trzeba uważać, żeby trigger nie wywołał innego zdarzenia, które z kolei uruchomi ten sam lub inny trigger, co może prowadzić do nieskończonej rekursji i zablokowania bazy danych.

5. **Wywoływanie funkcji**: W triggere można wywołać zdefiniowane wcześniej funkcje lub procedury składowane, aby zrealizować bardziej skomplikowaną logikę.

6. **Zarządzanie wyrażeniami warunkowymi**: Można użyć instrukcji IF lub CASE wewnątrz triggera, aby zdecydować, jakie działania należy podjąć w zależności od spełnienia określonych warunków.



## Docs

[Voice Assistant Use Cases & Examples for Business](https://masterofcode.com/blog/voice-assistant-use-cases-business-implementations-of-vuis-in-2021)
[Smart Operations for ER&I - Deloitte US.](https://www2.deloitte.com/us/en/pages/consulting/articles/smart-operations-industrial-revolution-4.html)
[What Are Smart Operations? - Oracle](https://www.oracle.com/scm/smart-operations/)


## NLP to SQL

+ [ln2sql - PyPI](https://pypi.org/project/ln2sql/)
+ [anaiscmateus/OpenAI-NLPtoSQL: This program is designed to translate natural language statements into SQL queries using OpenAI API, pandas library, and sqlalchemy. It is useful for those who are not familiar with SQL syntax and want to query databases using natural language.](https://github.com/anaiscmateus/OpenAI-NLPtoSQL)
+ [Setting a Natural Language to SQL Code Generator with Python | by Rami Krispin | Medium](https://medium.com/@rami.krispin/setting-a-natural-language-to-sql-code-generator-with-python-d267f40d7218)
+ 






## What is Voice Recognition?

+ [The Difference Between Speech and Voice Recognition](https://www.kardome.com/blog-posts/difference-speech-and-voice-recognition)

Voice recognition and speech recognition are similar in that a front-end audio device (microphone) translates a person’s voice into an electrical signal and then digitizes it. 

While speech recognition will recognize almost any speech (depending on language, accents, etc.), voice recognition applies to a machine’s ability to identify a specific users’ voice. 




[​Automatyzacja procesów biznesowych – co to jest? Dobre praktyki](https://cyrekdigital.com/pl/baza-wiedzy/automatyzacja-procesow-biznesowych/#:~:text=Automatyzacja%20proces%C3%B3w%20biznesowych%20%28znana%20te%C5%BC%20pod%20angielskim%20skr%C3%B3tem,kr%C3%B3tko%2C%20jest%20to%20zast%C4%85pienie%20manualnych%20prac%20rozwi%C4%85zaniami%20automatycznymi.)

> ## Metody automatyzacji procesów biznesowych
> 
> Do automatyzacji procesów biznesowych można stosować wiele różnorodnych metod. Najczęściej jednak wykorzystuje się sposoby i narzędzia, takie jak:
> 
> -   Robotyzacja procesów biznesowych (RPA, robotic process automation) polega na wykorzystaniu specjalnego oprogramowania do stworzenia robotów wykonujących powtarzalne zadania – wprowadzania danych, przetwarzania standardowych transakcji czy zarządzanie odpowiedziami na często zadawane pytania.
> -   Intelligent Process Automation (IPA, inteligentna automatyzacja procesów) łączy technologie RPA z zaawansowaną analizą danych, uczeniem maszynowym i sztuczną inteligencją, co pozwala automatyzować bardziej skomplikowane procesy biznesowe.
> -   Integration Platform as a Service (iPaaS, dosłownie „platforma integracyjna jako usługa”) to istniejących w chmurze zestaw narzędzi i usług umożliwiających łatwe tworzenie, wdrażanie i zarządzanie połączeniami między różnymi źródłami danych i aplikacjami. Jest stosowane do integracji różnych systemów i aplikacji w organizacji.
> -   Business Rules Management System (BRMS) służy do definiowania, zarządzania i wdrażania reguł biznesowych w pełni zautomatyzowany sposób.
> -   Automatyzacja procesów związanych z integracją danych, takich jak ekstrakcja, transformacja i ładowanie (ETL), pozwala efektywnie zarządzać danymi w organizacji poprzez synchronizację informacji z różnych źródeł.
> -   Document Management Systems to systemy zarządzania dokumentami. Wykorzystuje się je do automatyzacji procesów związanych z gromadzeniem, klasyfikacją, przetwarzaniem, archiwizacją i udostępnianiem dokumentów w organizacji.
> -   [Systemy CRM](https://cyrekdigital.com/pl/baza-wiedzy/system-crm/) pozwalają zautomatyzować procesy związane z zarządzaniem relacjami z klientami. Dzięki nim można np. zarządzać kontaktami, śledzić historii interakcji z klientami oraz przewidywać ich potrzeby.
> -   Oprogramowanie do zarządzania procesami biznesowymi (BPM) koncentruje się na całym cyklu życia procesu biznesowego, od modelowania i analizy przez implementację, do monitorowania i optymalizacji. Służy do tworzenia map przepływów pracy, które mogą być udoskonalane w celu zwiększenia wydajności organizacji.
> -   Sztuczną inteligencję i uczenie maszynowe wykorzystuje się do automatyzacji zadań wymagających zdolności do adaptacji i nauki na podstawie danych. Mogą być stosowane np. do automatycznego podejmowania decyzji, przewidywania wyników czy personalizacji doświadczeń klientów.
> -   Automatyzacja za pomocą integracji API polega na łączeniu różnych systemów i aplikacji za pomocą API (Application Programming Interface), co pozwala płynnie wymieniać dane między różnorodnymi technologiami, co jest ważne w firmach korzystających z wielu rodzajów oprogramowania.
> -   Workflow automation (automatyzacja przepływów pracy) polega na automatyzacji konkretnych sekwencji działań (przepływów pracy) w ramach określonych procesów biznesowych. Stosuje się do tego systemy workflow, które są szczególnie przydatne w organizacjach ze złożonymi strukturami zadaniowymi i procesowymi.

