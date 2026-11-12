// crop.swift in out x y w h radius outWidth: a piece of a picture, with rounded corners.
import AppKit
let a = CommandLine.arguments
let src = NSImage(contentsOfFile: a[1])!
var rect = CGRect(origin: .zero, size: src.size)
let cg = src.cgImage(forProposedRect: &rect, context: nil, hints: nil)!
let (x, y, w, h) = (Int(a[3])!, Int(a[4])!, Int(a[5])!, Int(a[6])!)
let radius = CGFloat(Double(a[7])!), outW = Int(a[8])!
let piece = cg.cropping(to: CGRect(x: x, y: y, width: w, height: h))!
let scale = CGFloat(outW) / CGFloat(w)
let outH = Int((CGFloat(h) * scale).rounded())
let ctx = CGContext(data: nil, width: outW, height: outH, bitsPerComponent: 8, bytesPerRow: 0, space: CGColorSpace(name: CGColorSpace.sRGB)!, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
ctx.interpolationQuality = .high
let box = CGRect(x: 0, y: 0, width: outW, height: outH)
ctx.addPath(CGPath(roundedRect: box, cornerWidth: radius * scale, cornerHeight: radius * scale, transform: nil))
ctx.clip()
ctx.draw(piece, in: box)
let rep = NSBitmapImageRep(cgImage: ctx.makeImage()!)
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: a[2]))
