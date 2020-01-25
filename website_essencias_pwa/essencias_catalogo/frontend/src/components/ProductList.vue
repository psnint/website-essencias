<template>
  <section class="productList__base">
    <div v-if="loading">
      Loading...
    </div>
    <div v-if="error">
      Couldn't fetch list of catalogues from server...
    </div>
    <ul v-if="!collectionId || collectionExists" class="productList__list">
      <ProductEntry v-for="product in products" :key="product.pk" :pk="product.pk"
              :title="product[`name_${$store.getters.lang}`]" :imgSrc="product.image"
              :link="`${!collectionId ? 'collection' : '/productDetail'}/${product.pk}`"
              :isProduct="Boolean(collectionId)" :productImages="product.productImages"
              />
    </ul>
  </section>
</template>

<script>

import ProductEntry from './ProductEntry.vue';
import API_URL from '../configs';

export default {
  name: 'ProductList',
  props: ['collectionId'],
  components: {
    ProductEntry,
  },
  data() {
    return {
      loading: false,
      error: null,
      // products: null,
    };
  },
  created() {
    this.requestProducts();
  },
  computed: {
    products() {
      return !this.collectionId
        ? this.$store.getters.catalogue
        : this.$store.getters.collection(this.collectionId);
    },
    collectionExists() {
      return this.$store.getters.collectionExists(this.collectionId);
    },
  },
  methods: {
    requestProducts() {
      this.error = null;
      this.loading = true;
      // catalogue view
      if (!this.collectionId) {
        // if catalogs not fetched yet
        if (this.products.length < 1) {
          fetch(`${API_URL}`)
            .then(res => res.json())
            .then((res) => {
              this.loading = false;
              this.$store.commit('updateCatalogue', res);
            }).catch(() => {
              this.loading = false;
              this.error = true;
            });
        } else {
          this.loading = false;
        }
      // collection view
      } else if (!this.collectionExists) {
        fetch(`${API_URL}/collection/?collectionId=${this.collectionId}`)
          .then(res => res.json())
          .then((res) => {
            this.loading = false;
            this.$store.commit('appendCollection', res);
          }).catch((err) => {
            this.loading = false;
            this.error = true;
            throw new Error(err);
          });
      } else {
        this.loading = false;
      }
    },
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "../css/default.scss";

  $moduleName: 'productList';

  .#{$moduleName} {
    &__base {

    }

    &__list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(50%, 1fr));
      grid-column-gap: 7px;
      max-width: 1024px;
      margin: 0 auto;
      padding: 0 7px;

      @include breakpoint-from(mq2) {
        grid-template-columns: repeat(auto-fit, minmax(40%, 1fr));
      }
      @include breakpoint-from(mq3) {
        grid-template-columns: repeat(auto-fit, minmax(30%, 1fr));
      }
      @include breakpoint-from(mq4) {
        grid-template-columns: repeat(auto-fit, minmax(20%, 1fr));
      }
    }
  }

</style>
