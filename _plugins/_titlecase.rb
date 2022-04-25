require 'liquid'
require 'uri'

module Jekyll
  module Titlecase
    def titlecase(words)
      return words.split(' ').map(&:capitalize).join(' ')
    end
  end
end

Liquid::Template.register_filter(Jekyll::Titlecase)
