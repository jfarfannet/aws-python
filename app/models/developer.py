from dataclasses import dataclass


@dataclass
class Developer:
    name: str
    role: str
    location: str
    about: str
    skills: list[str]
    experience_years: int
    email: str
    github: str
