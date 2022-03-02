const app = new Vue({
  el: "#anniv",
  data: {
    bonbons: 30,
    mnb: 30,
    mna: 8,
    selectedBox: -1,
    boxes: []
  },
  computed: {
    nb: {
      get: function () { return this.mnb; },
      set: function (newVal) {
        this.mnb = +newVal;
        this.bonbons = this.mnb;
        this.boxes = new Array(this.mna).fill(0);
      }
    },
    na: {
      get: function () { return this.mna; },
      set: function (newVal) {
        this.mna = +newVal;
        this.bonbons = this.mnb;
        this.boxes = new Array(this.mna).fill(0);
      }
    }
  },
  mounted: function () {
    this.reinitialiser();
  },
  methods: {
    mettreBonbon: function () {
      if (this.bonbons > 0) {
        const nbh = Math.floor(Math.random() * this.na);
        this.selectedBox = nbh;
        setTimeout(() => this.selectedBox = -1, 4000);
        this.boxes[nbh]++;
        this.bonbons--;
        this.$forceUpdate();
      }
    },
    distribuerBonbons: function () {
      while (this.bonbons > 0) {
        const nbh = Math.floor(Math.random() * this.na);
        this.boxes[nbh]++;
        this.bonbons--;
      }
      this.$forceUpdate();
    },
    reinitialiser: function() {
      this.na = this.na;
      this.bonbons = this.nb;
    }
  }
});