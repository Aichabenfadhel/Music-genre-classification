import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AudioService {
  private apiUrl = 'http://127.0.0.1:5001/svm/predict';

  constructor(private http: HttpClient) {}

  uploadAudio(file: File) {
    const formData = new FormData();
    formData.append('audio_file', file);
    return this.http.post<{ genre: string }>(this.apiUrl, formData);
  }
}
