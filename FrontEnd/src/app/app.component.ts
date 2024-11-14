import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  template: `   
    <main>
      <body>
          <router-outlet></router-outlet>
      </body>
    </main>
    `,
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'EventosScrapper';
}
