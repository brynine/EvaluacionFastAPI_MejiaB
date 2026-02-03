import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { VehiculoService } from '../../services/vehiculo.service';

@Component({
  selector: 'app-vehiculo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './vehiculo.component.html'
})
export class VehiculoComponent implements OnInit {

  vehiculo: any = {};
  vehiculos: any[] = [];

  constructor(private service: VehiculoService) {}

  ngOnInit(): void {
    this.cargar();
  }

  guardar() {
    this.service.guardar(this.vehiculo).subscribe(() => {
      this.vehiculo = {};
      this.cargar();
    });
  }

  cargar() {
    this.service.listar().subscribe(data => {
      this.vehiculos = data;
    });
  }
}
