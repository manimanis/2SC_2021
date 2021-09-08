class PagePersistance {
  constructor() {
    this.page_id = location.pathname;
    this.listeners = [];
    this.tokens = [];
    this.token = {};
    this.loadData();
  }

  validateToken(token_string) {
    try {
      const token = JSON.parse(token_string);
      const keys = ['data', 'date', 'name', 'token'];
      let valid = typeof token === 'object';
      const tokenKeys = Object.keys(token);
      valid = valid && tokenKeys
        .reduce((pv, cv) => pv && keys.includes(cv), valid);
      valid = valid && keys
        .reduce((pv, cv) => pv && tokenKeys.includes(cv), valid);
      valid = valid && typeof token.data === 'object' && Object
        .entries(token.data)
        .findIndex(arr => arr.findIndex(el => typeof el !== 'string') !== -1) === -1;
      return valid;
    } catch (err) {
      return false;
    }
  }

  setToken(token_string) {
    const token = JSON.parse(token_string);
    this.token.data = { ...token.data };
    this.token.date = token.date;
    this.notifyClients('load-token');
  }

  addListener(callback) {
    this.listeners.push(callback);
  }

  notifyClients(event_name) {
    this.listeners.forEach(listener => listener(event_name, this));
  }

  generateToken() {
    const generateRandomToken = (length) => {
      const ph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      let token = '';
      for (let i = 0; i < length; i++) {
        token += ph[Math.floor(Math.random() * ph.length)];
      }
      return token;
    };
    let token;
    do {
      token = generateRandomToken(8);
    } while (this.hasToken(token));
    return token;
  }

  hasToken(token) {
    return this.tokens.findIndex(token_obj => token_obj.token === token) !== -1;
  }

  createToken() {
    const token = this.generateToken();
    this.addToken(token);
    this.notifyClients('create');
  }

  addToken(token) {
    if (this.hasToken(token)) {
      throw new Error(`Token ${token} is already in use!`);
    }
    this.token = {
      name: token,
      token: token,
      date: new Date().toISOString(),
      data: {}
    };
    this.tokens.push(this.token);
    this.saveData();
  }

  loadByToken(token_name) {
    this.loadData();
    const idx1 = this.indexOf(token_name);
    if (idx1 === -1) {
      throw new Error(`Invalid token ${token_name}.`);
    }
    this.token = this.tokens[idx1];
    const idx2 = this.tokens.length - 1;
    if (idx1 !== idx2) {
      const temp = this.tokens[idx2];
      this.tokens[idx1] = temp;
      this.tokens[idx2] = this.token;
    }
    this.saveData();
    this.notifyClients('load-by-token');
  }

  findByName(token_name) {
    return this.tokens.find(t => t.name === token_name);
  }

  indexOf(token_name) {
    return this.tokens.findIndex(token_obj => token_obj.token === token_name);
  }

  loadData() {
    this.tokens = JSON.parse(localStorage.getItem(this.page_id)) || [];
    if (this.tokens.length === 0) {
      this.createToken();
    } else {
      this.token = this.tokens[this.tokens.length - 1];
    }
    this.notifyClients('load-data');
  }

  saveData() {
    localStorage.setItem(this.page_id, JSON.stringify(this.tokens));
    this.notifyClients('save-data');
  }

  setData(key, data) {
    if (typeof this.token.data !== 'object') {
      this.token.data = {};
    }
    this.token.data[key] = data;
    this.saveData();
  }

  getData(key) {
    if (!key) {
      return this.token.data;
    }
    return this.token.data[key];
  }

  resetData() {
    this.token.data = {};
    this.saveData();
    this.notifyClients('reset-data');
  }

  setName(name) {
    this.token.name = name;
    this.saveData();
  }

  getName() {
    return this.token.name;
  }
}


class ServerSaves {
  constructor(pagename) {
    this.storage_key = `${location.pathname}#server-saves`;
    this.pagename = pagename;
    this.url = 'saves.php';
    this.listeners = [];
    this.data = {};
    this.key = null;
    this.loadData();
  }

  loadData() {
    this.key = JSON.parse(localStorage.getItem(this.storage_key)) || '';
  }

  saveData() {
    localStorage.setItem(this.storage_key, JSON.stringify(this.key));
  }

  setKey(key) {
    this.key = key;
    this.saveData();
  }

  getKey() {
    return this.key;
  }

  addListener(listener) {
    this.listeners.push(listener);
  }

  _notify(event_name, data) {
    for (let listener of this.listeners) {
      listener(event_name, data, this);
    }
  }

  /**
   * 
   * @param {string} value
   * @returns {Promse} 
   */
  save(value) {
    return new Promise((resolve, reject) => {
      this._notify('saving', null);
      $.post(this.url, { key: this.key, value: value, pagename: this.pagename }, (data) => {
        if (data.resultat === 'ok') {
          this.data = data.data;
          this.key = this.getData('cle');
          this.saveData();
          this._notify('saved', data.data);
          resolve(data.data);
        } else {
          this._notify('error', data.message);
          reject(data.message);
        }
      }, 'json');
    });
  }

  /**
   * 
   * @returns {Promise}
   */
  load() {
    this._notify('loading', null);
    const url = `${this.url}?key=${encodeURIComponent(this.key)}&pagename=${encodeURIComponent(this.pagename)}`;
    return fetch(url, {
      "method": "GET",
      "headers": {
        "Accept": "application/json, text/javascript, */*; q=0.01"
      }
    })
      .then(response => response.json())
      .then(data => {
        if (data.resultat === 'ok') {
          this.data = data.data;
          this.key = this.getData('cle');
          this.saveData();
          this._notify('loaded', data.data);
          return data.data;
        } else {
          this._notify('error', data.message);
          throw new Error(data.message);
        }
      })
      .catch(error => {
        console.log(error);
        this._notify('error', error);
      });
  }

  reset() {
    const oldData = this.data;
    this.key = '';
    this.data = {};
    this.saveData();
    this._notify('reset', oldData);
  }

  getData(field) {
    return this.data[field];
  }
}

class UserInputSaver {
  constructor(node, localStore, serverStore) {
    this.node = $(node);
    this.localStore = localStore;
    this.serverStore = serverStore;
    this.buildUI();
    this.localStore.addListener((event_name) => {
      // console.log(event_name);
      this.update();
    });
    this.serverStore.addListener((event_name, data) => {
      // console.log(event_name, data);
      if (event_name === 'reset') {
        this._enableButtons(true);
        this.msg_span.text('Nouveau travail');
      } else if (event_name === 'loading') {
        this._enableButtons(false);
        this.msg_span.text('Chargement en cours...');
      } else if (event_name === 'saving') {
        this._enableButtons(false);
        this.msg_span.text('Enregistrement en cours...');
      } else if (event_name === 'loaded') {
        this._enableButtons(true);
        this.localStore.setToken(data['valeur']);
        this.msg_span.text(`Chargé. Clé : ${data['cle']} - Création : ${data['creation_date']} - MAJ : ${data['update_date']}`);
      } else if (event_name === 'saved') {
        this._enableButtons(true);
        this.localStore.setToken(data['valeur']);
        this.msg_span.text(`Enregistré. Clé : ${data['cle']} - Création : ${data['creation_date']} - MAJ : ${data['update_date']}`);
      } else if (event_name === 'error') {
        this.msg_span.text('Erreur : ' + data);
        this._enableButtons(true);
      }
    });
  }

  buildUI() {
    const thisObj = this;
    this.blk_control = $('<div>')
      .addClass('d-print-none')
      .appendTo(this.node);
    this.blk_saves_list = $('<div>')
      .addClass('my-2 d-print-none')
      .appendTo(this.node);
    this.btn_new = $('<button>')
      .addClass('btn btn-success ml-1')
      .text('Nouveau...')
      .appendTo(this.blk_saves_list)
      .on('click', (e) => {
        if (confirm('Choisir Annuler pour créer une nouvelle sauvegarde. Ok, sinon.')) {
          return;
        }
        this._saveToServer()
          .then(data => {
            this.serverStore.reset();
            this.localStore.resetData();
          })
          .catch(err => {
            this.serverStore.reset();
            this.localStore.resetData();
          });
      });
    this.btn_load = $('<button>')
      .addClass('btn btn-success ml-1')
      .text('Charger...')
      .appendTo(this.blk_saves_list)
      .on('click', (e) => {
        const key = prompt('Clé de sauvegarde');
        if (!key) {
          return;
        }
        this._loadFromServer(key);
      });
    this.btn_save = $('<button>')
      .addClass('btn btn-success ml-1')
      .text('Enregistrer')
      .appendTo(this.blk_saves_list)
      .on('click', (e) => {
        this._saveToServer();
      });
    this.search_link = $('<a>')
      .addClass('btn btn-secondary ml-1')
      .text('Chercher...')
      .attr('href', 'search.php?pagename=' + encodeURIComponent(this.serverStore.pagename))
      .attr('target', '_blank')
      .attr('rel', 'noopener')
      .appendTo(this.blk_saves_list);
    this.msg_span = $('<span>')
      .addClass('small ml-2')
      .appendTo(this.blk_saves_list);

    $('.save-content').each(function (index) {
      const input_ctrl = $(this);
      const placeholder = input_ctrl.attr('placeholder') || 'Taper un texte...';
      input_ctrl
        .wrap('<div></div>');
      const div_id = `save-content-${index}`;
      const parent_div = input_ctrl
        .parent('div')
        .attr('id', div_id)
        .addClass('save-content-div');
      input_ctrl
        .on('blur', (e) => {
          const input_ctrl = $(e.target);
          const parent_div = input_ctrl.parent('div');
          const div_id = parent_div.attr('id');
          thisObj.localStore.setData(div_id, input_ctrl.val());
          input_ctrl.hide();
          parent_div.find('pre')
            .show()
            .text(thisObj.localStore.getData(div_id) || placeholder);
        })
        .hide();
      $('<pre>')
        .text(thisObj.localStore.getData(div_id) || placeholder)
        .addClass('save-content-pre')
        .on('click', (e) => {
          const pre = $(e.target);
          const parent_div = pre.parent('div');
          const div_id = parent_div.attr('id');
          pre.hide();
          parent_div.find('.save-content')
            .show()
            .val(thisObj.localStore.getData(div_id) || '')
            .focus();
        })
        .appendTo(parent_div);
    });
  }

  update() {
    this._refreshInputs();
  }

  _saveToServer() {
    return this.serverStore.save(
      JSON.stringify(this.localStore.token) || "{}"
    )
      .then(data => console.log(data));
  }

  _loadFromServer(key) {
    this.serverStore.setKey(key);
    this.serverStore.load();
  }

  _enableButtons(enabled) {
    this.btn_new
      .attr('disabled', !enabled);
    this.btn_load
      .attr('disabled', !enabled);
    this.btn_save
      .attr('disabled', !enabled);
  }

  _refreshInputs() {
    const thisObj = this;
    $('.save-content-div')
      .each(function () {
        const div = $(this);
        const div_id = div.attr('id');
        const input_ctrl = div.find('.save-content');
        const pre = div.find('.save-content-pre');
        const placeholder = input_ctrl.attr('placeholder') || 'Taper un texte...';
        input_ctrl.val(thisObj.localStore.getData(div_id) || '');
        pre.text(thisObj.localStore.getData(div_id) || placeholder);

      });
  }
}
