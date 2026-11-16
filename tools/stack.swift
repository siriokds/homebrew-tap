// stack.swift in out radius outWidth x1 y1 w1 h1 [x2 y2 w2 h2 …]: pieces of one picture (pixels,
// from the top left) one under the other, the whole with rounded corners, scaled to outWidth.
// For a window whose middle is empty: its top and its status line, without the gap.
import AppKit
let a = CommandLine.arguments
let src = NSImage(contentsOfFile: a[1])!
var all = CGRect(origin: .zero, size: src.size)
let cg = src.cgImage(forProposedRect: &all, context: nil, hints: nil)!
let radius = CGFloat(Double(a[3])!), outW = Int(a[4])!
var pieces: [CGRect] = []
var k = 5
while k + 3 < a.count {
    pieces.append(CGRect(x: Double(a[k])!, y: Double(a[k + 1])!, width: Double(a[k + 2])!, height: Double(a[k + 3])!))
    k += 4
}
let width = pieces.map(\.width).max()!
let height = pieces.map(\.height).reduce(0, +)
let scale = CGFloat(outW) / width
let outH = Int((height * scale).rounded())
let ctx = CGContext(data: nil, width: outW, height: outH, bitsPerComponent: 8, bytesPerRow: 0, space: CGColorSpace(name: CGColorSpace.sRGB)!, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
ctx.interpolationQuality = .high
ctx.addPath(CGPath(roundedRect: CGRect(x: 0, y: 0, width: outW, height: outH), cornerWidth: radius * scale, cornerHeight: radius * scale, transform: nil))
ctx.clip()
var top = CGFloat(outH)
for piece in pieces {
    let h = piece.height * scale
    top -= h
    ctx.draw(cg.cropping(to: piece)!, in: CGRect(x: 0, y: top, width: piece.width * scale, height: h))
}
let rep = NSBitmapImageRep(cgImage: ctx.makeImage()!)
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: a[2]))
