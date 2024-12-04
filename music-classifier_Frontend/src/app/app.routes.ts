import { Routes } from '@angular/router';
import { FileUploadComponent } from './file-upload/file-upload.component';
import { VggComponent } from './vgg/vgg.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
    { path: '', component: HomeComponent }, 
    { path: 'svm', component: FileUploadComponent },
    { path: 'vgg', component: VggComponent }
];
