# Group Based Chat:
  
  It is a C based program build using of Socket Programming.

  In this program we can join many client to a server and can share messages between each other and form a group for chatting.

## Running the code:
  
  First we have to compile both server.c file and client.c file using;
  
  To compile server file run the following command 
  ```
  gcc server.c -pthread -o server
  ```
  To compile client file run the following command
  ```
  gcc client.c -pthread -o client
  ```
  
  To find out the performance measurements run the following command
  ```
  python time_run.py
  ```
  
## Results
  
  Results obtained when only one person is sending the messege;

 | No | No of Clients | Time taken |
 | -- | ------------- | ---------- |
 | 1. |      10       |   50.9ms   |   
 | 2. |      20       |   51.55ms  |
 | 3. |      30       |   51.97ms  |
 | 4. |      40       |   52.2ms   |
 | 5. |      50       |   54.19ms  |
 | 6. |      60       |   55.36ms  |
 | 7. |      70       |   40.35ms  |
 | 8. |      80       |   65.4ms   |
 | 9. |      90       |   86.89ms  |
