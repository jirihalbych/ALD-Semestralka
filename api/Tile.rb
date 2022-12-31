# frozen_string_literal: true

# Holds data about Tile type and its neighbours
class Tile
  attr_accessor :above, :bellow, :left, :right, :type

  def initialize(type = [-1, -1, -1, -1])
    @type = type
  end
end
