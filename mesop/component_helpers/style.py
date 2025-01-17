from dataclasses import dataclass
from typing import Literal

import mesop.protos.ui_pb2 as pb

ContentAlignmentValues = Literal[
  "center",
  "start",
  "end",
  "flex",
  "flex",
  "left",
  "right",
  "space-between",
  "space-around",
  "space-evenly",
  "stretch",
]
ItemAlignmentValues = Literal[
  "normal",
  "stretch",
  "center",
  "start",
  "end",
]
OverflowValues = Literal["visible", "hidden", "clip", "scroll", "auto"]


@dataclass(kw_only=True)
class BorderSide:
  """
  Represents the style of a single side of a border in a UI component.

  Attributes:
      width: The width of the border. Can be specified as an integer value representing pixels,
                                a string with a unit (e.g., '2em'), or None for no width.
      color: The color of the border, represented as a string. This can be any valid CSS color value,
                          or None for no color.
      style: The style of the border, which can be 'none' for no border, 'solid' for a solid line.
  """

  width: int | str | None = None
  color: str | None = None
  style: Literal["none", "solid"] | None = None


@dataclass(kw_only=True)
class Border:
  """
  Defines the border styles for each side of a UI component.

  Attributes:
      top: Style for the top border.
      right: Style for the right border.
      bottom: Style for the bottom border.
      left: Style for the left border.
  """

  top: BorderSide | None = None
  right: BorderSide | None = None
  bottom: BorderSide | None = None
  left: BorderSide | None = None


@dataclass(kw_only=True)
class _EdgeInsets:
  top: int | str | None = None
  right: int | str | None = None
  bottom: int | str | None = None
  left: int | str | None = None


@dataclass(kw_only=True)
class Margin(_EdgeInsets):
  """
  Defines the margin space around a UI component.

  Attributes:
      top: Top margin (note: `2` is the same as `2px`)
      right: Right margin
      bottom: Bottom margin
      left: Left margin
  """

  top: int | str | None = None
  right: int | str | None = None
  bottom: int | str | None = None
  left: int | str | None = None


@dataclass(kw_only=True)
class Padding(_EdgeInsets):
  """
  Defines the padding space around a UI component.

  Attributes:
      top: Top padding (note: `2` is the same as `2px`)
      right: Right padding
      bottom: Bottom padding
      left: Left padding
  """

  top: int | str | None = None
  right: int | str | None = None
  bottom: int | str | None = None
  left: int | str | None = None


@dataclass(kw_only=True)
class Style:
  """
  Represents the style configuration for a UI component.

  Attributes:
      align_content: Aligns the flexible container's items on the cross-axis. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content).
      align_items: Specifies the default alignment for items inside a flexible container. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items).
      background: Sets the background color or image of the component. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/background).
      border: Defines the border properties for each side of the component. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/border).
      border_radius: Defines the border radius. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius).
      box_shadow: Defines the box shadow. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow).
      box_sizing: Defines the box sizing. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing).
      color: Sets the color of the text inside the component. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/color).
      column_gap: Sets the gap between columns. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap).
      columns: Specifies the number of columns in a multi-column element. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/columns).
      cursor: Sets the mouse cursor. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor).
      display: Defines the display type of the component. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/display).
      flex_basis: Specifies the initial length of a flexible item. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis).
      flex_direction: Establishes the main-axis, thus defining the direction flex items are placed in the flex container. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction).
      flex_grow: Defines the ability for a flex item to grow if necessary. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow).
      flex_shrink: Defines the ability for a flex item to shrink if necessary. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink).
      flex_wrap: Allows flex items to wrap onto multiple lines. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap).
      font_family: Specifies the font family. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family).
      font_size: Sets the size of the font. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size).
      font_style: Specifies the font style for text. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style).
      font_weight: Sets the weight (or boldness) of the font. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight).
      gap: Sets the gap. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/gap).
      grid_area: Sets the grid area. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-area).
      grid_column_start: Sets the grid column start. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-start).
      grid_column_end: Sets the grid column end. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-end).
      grid_row_start: Sets the grid row start. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-start).
      grid_row_end: Sets the grid row end. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-end).
      grid_template_areas: Sets the grid template areas; each element is a row. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas).
      grid_template_columns: Sets the grid template columns. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns).
      grid_template_rows: Sets the grid template rows. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows).
      height: Sets the height of the component. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/height).
      justify_content: Aligns the flexible container's items on the main-axis. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content).
      letter_spacing: Increases or decreases the space between characters in text. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing).
      line height: Set the line height (relative to the font size). See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height).
      margin: Sets the margin space required on each side of an element. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/margin).
      outline: Sets the outline property. Note: `input` component has default browser stylings. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/outline).
      overflow_x: Specifies the handling of overflow in the horizontal direction. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-x).
      overflow_y: Specifies the handling of overflow in the vertical direction. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-y).
      padding: Sets the padding space required on each side of an element. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/padding).
      position: Specifies the type of positioning method used for an element (static, relative, absolute, fixed, or sticky). See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/position).
      row_gap: Sets the gap between rows. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap).
      text_align: Specifies the horizontal alignment of text in an element. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align).
      text_decoration: Specifies the decoration added to text. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration).
      text_overflow: Specifies how overflowed content that is not displayed should be signaled to the user. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow).
      white_space: Specifies how white space inside an element is handled. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space).
      width: Sets the width of the component. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/width).
      z-index: Sets the z-index of the component. See [MDN doc](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index).
  """

  # For literal properties, make the most commonly used option the first literal
  # element, as it will be used as the default value by the editor when creating that property.

  align_content: ContentAlignmentValues | None = None
  align_items: ItemAlignmentValues | None = None
  background: str | None = None
  border: Border | None = None
  border_radius: int | str | None = None
  box_shadow: str | None = None
  box_sizing: str | None = None
  color: str | None = None
  column_gap: int | str | None = None
  columns: int | str | None = None
  cursor: str | None = None
  display: Literal[
    # precomposed values
    "block",
    "inline",
    "inline-block",
    "flex",
    "inline-flex",
    "grid",
    "inline-grid",
    # box generation
    "none",
    "contents",
  ] | None = None
  flex_basis: str | None = None
  flex_direction: Literal[
    "row",
    "row-reverse",
    "column",
    "column-reverse",
  ] | None = None
  flex_grow: int | None = None
  flex_shrink: int | None = None
  flex_wrap: Literal["nowrap", "wrap", "wrap-reverse"] | None = None
  font_family: str | None = None
  font_size: int | str | None = None
  font_style: Literal["italic", "normal"] | None = None
  font_weight: Literal[
    "bold",
    "normal",
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800,
    900,
  ] | None = None
  gap: int | str | None = None
  grid_area: str | None = None
  grid_column_start: int | None = None
  grid_column_end: int | None = None
  grid_row_start: int | None = None
  grid_row_end: int | None = None
  grid_template_areas: list[str] | None = None
  grid_template_columns: str | None = None
  grid_template_rows: str | None = None
  height: int | str | None = None
  justify_content: ContentAlignmentValues | None = None
  justify_items: ItemAlignmentValues | None = None
  letter_spacing: int | str | None = None
  line_height: str | None = None
  margin: Margin | None = None
  outline: str | None = None
  overflow_x: OverflowValues | None = None
  overflow_y: OverflowValues | None = None
  padding: Padding | None = None
  position: Literal[
    "static",
    "relative",
    "absolute",
    "fixed",
    "sticky",
  ] | None = None
  row_gap: int | str | None = None
  text_align: Literal[
    "start",
    "end",
    "left",
    "right",
    "center",
  ] | None = None
  text_decoration: Literal["underline", "none"] | None = None
  text_overflow: Literal["ellipsis", "clip"] | None = None
  white_space: Literal[
    "normal",
    "nowrap",
    "pre",
    "pre-wrap",
    "pre-line",
    "break-spaces",
  ] | None = None
  width: int | str | None = None
  z_index: int | None = None


def to_style_proto(s: Style) -> pb.Style:
  return pb.Style(
    align_content=s.align_content,
    align_items=s.align_items,
    background=s.background,
    border=_map_border(s.border),
    border_radius=_px_str(s.border_radius),
    box_shadow=s.box_shadow,
    box_sizing=s.box_sizing,
    color=s.color,
    column_gap=_px_str(s.column_gap),
    columns=str(s.columns),
    cursor=s.cursor,
    display=s.display,
    flex_basis=s.flex_basis,
    flex_direction=s.flex_direction,
    flex_grow=s.flex_grow,
    flex_shrink=str(s.flex_shrink),
    flex_wrap=s.flex_wrap,
    font_family=s.font_family,
    font_size=_px_str(s.font_size),
    font_style=s.font_style,
    font_weight=_map_font_weight(s.font_weight),
    gap=_px_str(s.gap),
    grid_area=s.grid_area,
    grid_column_start=s.grid_column_start,
    grid_column_end=s.grid_column_end,
    grid_row_start=s.grid_row_start,
    grid_row_end=s.grid_row_end,
    grid_template_areas=s.grid_template_areas,
    grid_template_columns=s.grid_template_columns,
    grid_template_rows=s.grid_template_rows,
    height=_px_str(s.height),
    justify_content=s.justify_content,
    justify_items=s.justify_items,
    letter_spacing=_px_str(s.letter_spacing),
    line_height=str(s.line_height),
    margin=_map_edge_insets(s.margin),
    outline=s.outline,
    overflow_x=s.overflow_x,
    overflow_y=s.overflow_y,
    padding=_map_edge_insets(s.padding),
    position=s.position,
    row_gap=_px_str(s.row_gap),
    text_align=s.text_align,
    text_decoration=s.text_decoration,
    text_overflow=s.text_overflow,
    white_space=s.white_space,
    width=_px_str(s.width),
    z_index=s.z_index,
  )


def _map_font_weight(fw: int | str | None) -> str:
  if fw is None:
    return ""
  return str(fw)


def _map_edge_insets(e: _EdgeInsets | None) -> pb.EdgeInsets | None:
  if e is None:
    return None
  return pb.EdgeInsets(
    top=_px_str(e.top),
    bottom=_px_str(e.bottom),
    left=_px_str(e.left),
    right=_px_str(e.right),
  )


def _map_border(b: Border | None) -> pb.Border | None:
  if b is None:
    return None
  return pb.Border(
    top=_map_border_side(b.top),
    bottom=_map_border_side(b.bottom),
    left=_map_border_side(b.left),
    right=_map_border_side(b.right),
  )


def _map_border_side(bs: BorderSide | None) -> pb.BorderSide | None:
  if bs is None:
    return None
  return pb.BorderSide(width=_px_str(bs.width), color=bs.color, style=bs.style)


def _px_str(int_or_str: int | str | None) -> str | None:
  if isinstance(int_or_str, int):
    return str(int_or_str) + "px"
  return int_or_str
