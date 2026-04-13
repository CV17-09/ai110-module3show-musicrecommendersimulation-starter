```mermaid
flowchart TD
    A[User Profile (Preferences)] --> E[Scoring Logic]
    B[songs.csv] --> C[Read Songs]
    C --> D[Loop Through Each Song]
    D --> E
    E --> F[Calculate Score for Song]
    F --> G[Store Song Score]
    G --> H[Sort Songs by Score]
    H --> I[Top K Recommendations]