from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Notes API - FastAPI Starter")

class Note(BaseModel):
    id: int
    title: str
    content: str

class NoteCreate(BaseModel):
    title: str
    content: str

# In-memory storage
_notes: List[Note] = []
_next_id = 1

@app.get("/notes", response_model=List[Note])
def list_notes():
    return _notes

@app.post("/notes", response_model=Note, status_code=201)
def create_note(note_in: NoteCreate):
    global _next_id
    note = Note(id=_next_id, title=note_in.title, content=note_in.content)
    _notes.append(note)
    _next_id += 1
    return note

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for n in _notes:
        if n.id == note_id:
            return n
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note_in: NoteCreate):
    for idx, n in enumerate(_notes):
        if n.id == note_id:
            updated = Note(id=note_id, title=note_in.title, content=note_in.content)
            _notes[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    for idx, n in enumerate(_notes):
        if n.id == note_id:
            _notes.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Note not found")

if __name__ == "__main__":
    # Executa com uvicorn programaticamente para conveniência
    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=False)
