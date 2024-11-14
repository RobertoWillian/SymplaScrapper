import { Component } from '@angular/core';
import { Eventos } from './eventos';
import { EventosService } from './eventos.service';
import { firstValueFrom } from 'rxjs';
import { FormControl, ReactiveFormsModule  } from '@angular/forms';

@Component({
  selector: 'app-eventos',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './eventos.component.html',
  styleUrls: ['./eventos.component.css']
})
export class EventosComponent {
  eventos: Eventos[] = [];
  isLoading: boolean = false;
  imagemPath = 'app/assets/estrela.png';

  searchTerm = new FormControl('');

  constructor(
    private eventosService: EventosService,
  ) {}

  async getAllEventos() {
    this.eventos = []
    this.isLoading = true; 
    try {
      const response = await firstValueFrom(this.eventosService.getAll());
      if (response) {
        this.eventos = response;
      }
    } catch (error) {
      console.error('Erro ao carregar eventos:', error);
    } finally {
      this.isLoading = false; 
    }
  }

  filteredEventos() {
    return this.eventos.filter(evento => 
      evento.Titulo.toLowerCase().includes((this.searchTerm.value || '').toLowerCase()) ||
      evento.Endereco.toLowerCase().includes((this.searchTerm.value || '').toLowerCase())
    );
  }

}