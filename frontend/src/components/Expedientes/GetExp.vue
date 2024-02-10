<template>
    <div>
        <section class="intro">
            <div class="gradient-custom-2 h-100">
              <div class="mask d-flex align-items-center h-100">
                <div class="container">
                  <div class="row justify-content-center">
                    <div class="col-12">
                      <div class="table-responsive">
                        <table class="table table-dark table-bordered mb-0">
                          <thead>
                            <tr>
                              <th scope="col">Numero de expediente</th>
                              <th scope="col">Numero de pago</th>
                              <th scope="col">Año</th>
                              <th scope="col">Detalles</th>
                              <th scope="col">Proovedor</th>
                              <th scope="col">Costo</th>
                              <th scope="col">Acciones</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="expediente in expedientes" :key="expediente.id">
                              <th scope="row">
                                {{ expediente.nro_expediente}}</th>
                              <td>{{expediente.nro_pago}}</td>
                              <td>{{expediente.año}}</td>
                              <td>{{expediente.detalles}}</td>
                              <td>{{expediente.provedor}}</td>
                              <td>${{expediente.valor}}</td>
                              <td> &nbsp;
                                <button class="btn btn-danger" @click="Eliminar(expediente.id, expediente.nro_expediente)"> 
                                <i class="fa-solid fa-trash"></i> 
                                </button>
                                </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
    </div>
</template>

<script  lang="ts">
import axios from 'axios'
import { confirmar } from '../../Functions/Funciones.js'
export default {
    data() {
        return{
            expedientes: null,
        }
    },
    mounted(){
        this.GetExp();
    },
    methods: {
        GetExp() {
            axios.get('http://127.0.0.1:8000/api/expediente/').then(
                response => {
                    this.expedientes = response.data
                }).catch(error => {console.error()}
            );
        },
        Eliminar(id: any, descripcion: any, url='http://127.0.0.1:8000/api/expediente', mensaje = 'Expediente eliminado', href ='/expedientes'){
            confirmar(id, descripcion, url, mensaje, href)
        }
    }
}

</script>

<style scoped>

</style>