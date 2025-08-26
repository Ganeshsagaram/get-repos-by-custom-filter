from fastapi import FastAPI, Query
from github import Github
from datetime import datetime
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

app = FastAPI()

# 🔑 Authenticate with your GitHub personal access token
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
g = Github(ACCESS_TOKEN)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test-cors")
def test_cors():
    print("testing")
    return {"msg": "CORS test"}


@app.get("/repos")
def get_repos(
    language: str = Query("Python", description="Programming language"),
    stars: int = Query(100, description="Minimum stars"),
    created_after: str = Query("2018-05-05", description="Created after (YYYY-MM-DD)"),
    limit: int = Query(10, description="Limit number of results")
):
    """
    Get repositories from GitHub with filters.
    Example query:
    /repos?language=Python&stars=500&created_after=2020-01-01&limit=5
    """

    # Validate created_after format
    try:
        datetime.strptime(created_after, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    # Build GitHub search query
    query = f"language:{language} created:>={created_after} stars:>={stars}"

    repos = g.search_repositories(query=query, sort="stars", order="desc")
    limit=min(limit, repos.totalCount)  # Ensure we don't exceed total count
    print(limit)
    results = []
    for repo in repos[:limit]:
        results.append({
            "name": repo.full_name,
            "url": repo.html_url,
            "created_at": repo.created_at.strftime("%Y-%m-%d"),
            "stars": repo.stargazers_count,
            "description": repo.description
        })

    return {"query": query, "repos": results}

# print(dir(Github))