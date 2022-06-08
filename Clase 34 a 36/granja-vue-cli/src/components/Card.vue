<template>
  <div class="card">
    <div class="card-title">{{ prod.description }}</div>
    <div class="card-body">
      <i :class="`icofont-10x icofont-${prod.icon}`"></i>
      <form>
        <div class="row">
          <div class="cell">
            <label>Tipo:</label>
          </div>
          <div class="cell">
            <em>{{ prod.category }}</em>
          </div>
        </div>
        <div class="row">
          <div class="cell">
            <label>Precio:</label>
          </div>
          <div class="cell">${{ prod.price }}</div>
        </div>
        <div class="row">
          <div class="cell">
            <label>Cantidad:</label>
          </div>
          <div class="cell">
            <input type="number" v-model="quantity" />
          </div>
        </div>
      </form>
    </div>
    <div class="card-footer">
      <button @click="addToCart(prod.description, quantity)" class="btn btn-light">
        Agregar al carrito
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['prod', 'addToCart', 'index'],
  data () {
    return {
      quantity: 1
    }
  }
}
</script>
