var $ = require('jquery')

const UserSearch = {
  renderSuggestions (context) {
    return `<div><img src="${context.default_avatar}" alt="" class="circled"> ${context.username}</div>`
  },

  findMatches (q, cb, acb) {
    $.get('/api/users?search=' + q, function (results) {
      acb(results)
    })
  },

  getDisplay (context) {
    return context.username
  },

  init () {
    $('.typeahead').typeahead({
      hint: true,
      highlight: true,
      minLength: 1
    }, {
      name: 'states',
      source: this.findMatches,
      display: this.getDisplay,
      templates: {
        suggestion: this.renderSuggestions
      }
    })
  }
}

UserSearch.init()
