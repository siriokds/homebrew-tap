cask "sparkedit" do
  version "2.1.1,361"
  sha256 "0ef6813d6ecdc9df8f4b027ecd5ed3d4baa9436e622e858638b372d5325da408"

  url "https://github.com/siriokds/homebrew-tap/releases/download/sparkedit-#{version.csv.first}-#{version.csv.second}/SparkEdit-#{version.csv.first}-#{version.csv.second}.zip"
  name "SparkEdit"
  desc "Text editor whose tabs are miniatures of their pages"
  homepage "https://github.com/siriokds/homebrew-tap"

  depends_on arch: :arm64
  depends_on macos: :sonoma

  app "SparkEdit.app"
  # spk, as CotEditor's cot: `spk file` opens the file in SparkEdit.
  binary "#{appdir}/SparkEdit.app/Contents/SharedSupport/bin/spk"

  uninstall quit: "com.siriokds.sparkedit"

  # No zap: SparkEdit's folder holds the user's notes and session, never deleted by Homebrew.

  caveats <<~EOS
    SparkEdit is not notarized by Apple. Open it once from Applications: macOS
    stops it; then System Settings > Privacy & Security, "Open Anyway".
    Until then the spk command is stopped too.

    In the shell: spk file opens the file in SparkEdit (spk -h for the rest).

    Colours for code (optional): the dual-syntax plugin, from another tap:
      brew install siriokds/dual-viewers/dual-syntax
    Settings > Text says whether SparkEdit found it.
  EOS
end
