import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class VehiculoService {

  private url = 'http://localhost:8000/vehiculos';

  constructor(private http: HttpClient) {}

  guardar(data: any) {
    return this.http.post(this.url, data);
  }

  listar() {
    return this.http.get<any[]>(this.url);
  }
}
