cask "sparkedit" do
  version "2.0.0,172"
  sha256 "6779c45d8d98f307cef5cd5e6888b4d8886bcba5369798f0f5b08a057baeb864"

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
  EOS
end
