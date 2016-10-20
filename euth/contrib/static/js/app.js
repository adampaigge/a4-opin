var ReactComments = require('../../../comments/static/comments/react_comments.js')
var ReactParagraphs = require('../../../documents/static/documents/ParagraphBox.js')
var ReactRatings = require('../../../ratings/static/ratings/react_ratings.jsx')
var ReactLanguageSwitch = require('../../../dashboard/static/language_switch/react_language_switch.jsx')

module.exports = {
  'renderComment': ReactComments.renderComment,
  'renderRatings': ReactRatings.renderRatings,
  'renderLanguageSwitch': ReactLanguageSwitch.renderLanguageSwitch,
  'renderParagraphs': ReactParagraphs.renderParagraphs
}
