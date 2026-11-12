// keyto.swift pid keycode [cmd]: a key sent to one program, without bringing it to the front.
import CoreGraphics
import Foundation
let a = CommandLine.arguments
let pid = pid_t(a[1])!, code = CGKeyCode(a[2])!
let flags: CGEventFlags = a.count > 3 && a[3] == "cmd" ? .maskCommand : []
for down in [true, false] {
    let e = CGEvent(keyboardEventSource: nil, virtualKey: code, keyDown: down)!
    e.flags = flags
    e.postToPid(pid)
    usleep(60000)
}
