import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Eventos } from './eventos';

@Injectable({
  providedIn: 'root'
})

export class EventosService {

  //Passa o endereço da nossa Api (Tem que colocar isso em um arquivo depois, ta paia assim.)
  private apiUrl: string = "http://127.0.0.1:8000";

  constructor(private http: HttpClient, private params: HttpParams) { 
    this.apiUrl
  }

  getAll(): Observable<Eventos[]> {
    return this.http.get<Eventos[]>(`${this.apiUrl}/eventos`);
  }


}