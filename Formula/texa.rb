class Texa < Formula
  desc "Small text editor for the terminal, in the spirit of nano and vim"
  homepage "https://github.com/siriokds/homebrew-tap"
  version "0.1.6"

  depends_on arch: :arm64
  depends_on :macos

  # The program already built: nothing is compiled on install. The Linux archive
  # will join the macOS one.
  on_macos do
    on_arm do
      url "https://github.com/siriokds/homebrew-tap/releases/download/texa-#{version}/texa-#{version}-macos-arm64.tar.gz"
      sha256 "6fc2e1b8bb670197cf3b7450ac11b1e8e52b3c971c4c3d5a11c4091c7c6b4c6d"
    end
  end

  def install
    bin.install "texa"
    doc.install "CREDITS.md"
  end

  test do
    assert_match "texa #{version}", shell_output("#{bin}/texa --version")
  end
end
