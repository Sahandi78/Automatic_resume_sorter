
from pydantic import BaseModel, Field


class PersonalInformation(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    location: str | None = None


class Education(BaseModel):
    degree: str | None = None
    field: str | None = None
    institution: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    gpa: str | None = None


class Experience(BaseModel):
    job_title: str | None = None
    company: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    responsibilities: list[str] = Field(default_factory=list)


class Publication(BaseModel):
    title: str | None = None
    authors: list[str] = Field(default_factory=list)
    venue: str | None = None
    year: str | None = None
    doi_or_url: str | None = None
    description: str | None = None


class LanguageTest(BaseModel):
    language: str | None = None
    test_name: str | None = None
    score: str | None = None
    test_date: str | None = None


class Projects(BaseModel):
    title: str | None = None
    description: str | None = None
    

class Resume(BaseModel):
    personal_information: PersonalInformation = Field(
        default_factory=PersonalInformation
    )

    summary: str | None = None

    skills: list[str] = Field(default_factory=list)

    education: list[Education] = Field(default_factory=list)

    experience: list[Experience] = Field(default_factory=list)

    projects: list[Projects] = Field(default_factory=list)

    publications: list[Publication] = Field(default_factory=list)

    academic_courses: list[str] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)

    languages: list[str] = Field(default_factory=list)

    language_tests: list[LanguageTest] = Field(default_factory=list)

    honors_and_awards: list[str] = Field(default_factory=list)


class CoreProfile(BaseModel):
    personal_information: PersonalInformation = Field(
        default_factory=PersonalInformation
    )
    summary: str | None = None
    education: list[Education] = Field(default_factory=list)
    experience: list[Experience] = Field(default_factory=list)
    


class TechnicalProfile(BaseModel):
    skills: list[str] = Field(default_factory=list)
    projects: list[Projects] = Field(default_factory=list)
    academic_courses: list[str] = Field(default_factory=list)


class AdditionalQualifications(BaseModel):
    publications: list[Publication] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
    language_tests: list[LanguageTest] = Field(default_factory=list)
    honors_and_awards: list[str] = Field(default_factory=list)
