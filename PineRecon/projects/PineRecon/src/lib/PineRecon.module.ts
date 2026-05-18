import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PineReconComponent } from './components/PineRecon.component';
import { RouterModule, Routes } from '@angular/router';

import {MaterialModule} from './modules/material/material.module';
import {FlexLayoutModule} from '@angular/flex-layout';

import {FormsModule} from '@angular/forms';

const routes: Routes = [
    { path: '', component: PineReconComponent }
];

@NgModule({
    declarations: [PineReconComponent],
    imports: [
        CommonModule,
        RouterModule.forChild(routes),
        MaterialModule,
        FlexLayoutModule,
        FormsModule,
    ],
    exports: [PineReconComponent]
})
export class PineReconModule { }
