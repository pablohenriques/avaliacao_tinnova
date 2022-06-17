import Vue from 'vue'
import Vuex from 'vuex'
import http from '@/http'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
        veiculos: null,
        naoVendidos:null,
        quantidadeSemanal: null,
        quantidadeDecada: null,
        quantidadeFabricante: null
  },
  getters: {
        listaVeiculos: state => state.veiculos,
        valorNaoVendidos: state => state.naoVendidos,
        valorSemanal: state => state.quantidadeSemanal,
        listaFabricante: state => state.quantidadeFabricante,
        listaDecada: state => state.quantidadeDecada

  },
  mutations: {
        DEFINIR_LISTA_VEICULOS(state, {veiculos}) {
          state.veiculos = veiculos;
        },
        DEFINIR_NAO_VENDIDOS(state, {naoVendidos}){
            state.naoVendidos = naoVendidos;
        },
        DEFINIR_SEMANAL(state, {quantidadeSemanal}){
            state.quantidadeSemanal = quantidadeSemanal;
        },
        DEFINIR_LISTA_FABRICANTES(state, {quantidadeFabricante}){
            state.quantidadeFabricante = quantidadeFabricante;
        },
        DEFINIR_LISTA_DECADA(state, {quantidadeDecada}){
            state.quantidadeDecada = quantidadeDecada;
        }
  },
  actions: {
    retornarTodosVeiculos({commit}) {
      return new Promise((resolve, reject) => {
        http.get('veiculos/')
            .then((response) => {
              let dados = response.data;
              commit('DEFINIR_LISTA_VEICULOS', {veiculos: dados});
              resolve(response)
            })
            .catch((error) => {
              reject(error);
            });
      });
    },

    deletarVeiculo({commit}, id_veiculo) {
      return new Promise((resolve, reject) => {
        http.delete(`veiculos/${id_veiculo}`)
            .then((response) => {
              resolve(response);
            })
            .catch((error) => {
              reject(reject);
            });
      })
    },

      atualizarParcialVeiculo({commit}, dados) {
        return new Promise((resolve, reject) => {
            http.patch(`veiculos/${dados["id"]}`, dados["corpo"])
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => {
                    reject(error)
                })
        })
      },

      cadastrarVeiculo({commit}, dados) {
        return new Promise((resolve, reject) => {
            http.post(`veiculos/`, dados)
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => {
                    reject(error)
                })
        });
      },

      retornarDados({commit}) {
          return new Promise((resolve, reject) => {
              http.get(`veiculos/dados`)
                  .then((response) => {
                      let qtdFabriacante = response.data["quantidade_fabricante"]
                      let qtdDecada = response.data["quantidade_decada"]
                      let qtdSemanal = response.data["quantidade_semana"]
                      let qtdNaoVendida = response.data["quantidade_nao_vendida"]

                      commit('DEFINIR_NAO_VENDIDOS', {naoVendidos: qtdNaoVendida})
                      commit('DEFINIR_SEMANAL', {quantidadeSemanal: qtdSemanal})
                      commit('DEFINIR_LISTA_FABRICANTES', {quantidadeFabricante: qtdFabriacante})
                      commit('DEFINIR_LISTA_DECADA', {quantidadeDecada: qtdDecada})
                      resolve(response)
                  })
                  .catch((error) => {
                      reject(error)
                  })
          });
      }
  },
  modules: {
  }
})
